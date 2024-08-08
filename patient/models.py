import qrcode
from cryptography.fernet import Fernet
import base64
from django.core.files.base import ContentFile
from django.conf import settings
from django.utils import timezone
from django.db import models
from clinical.models import Clinical
import uuid
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from io import BytesIO
from datetime import date, datetime

type_gender = (
    ('m', 'M'),
    ('f', 'F'),
)

class Patient(models.Model):
    
    nom = models.CharField(max_length=1000)
    post_nom = models.CharField(max_length=1000)
    prenom = models.CharField(max_length=1000)
    adresse = models.CharField(max_length=1000)
    genre = models.CharField(max_length=100, choices=type_gender, default='m')
    date_birth = models.DateField()
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, blank=True)
    date_register = models.DateField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    secret_key = models.CharField(max_length=100, blank=True, null=True)
    age_en_mois = models.IntegerField(blank=True, null=True)
    age_en_annees = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculer l'âge du patient en mois et en années
        if self.date_birth:
            if isinstance(self.date_birth, str):
                self.date_birth = datetime.strptime(self.date_birth, '%Y-%m-%d').date()

            today = date.today()
            birth_date = self.date_birth
            age_years = today.year - birth_date.year
            age_months = (today.year - birth_date.year) * 12 + (today.month - birth_date.month)

            if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
                age_years -= 1

            self.age_en_annees = age_years
            self.age_en_mois = age_months

        # Générer un code unique si non défini
        if not self.code:
            self.code = str(uuid.uuid4()).replace('-', '').upper()[:10]

        # Générer une clé secrète pour le chiffrement de type Vigenère
        if not self.secret_key:
            self.secret_key = base64.urlsafe_b64encode(Fernet.generate_key()).decode()

        # Chiffrer les informations du patient
        patient_info = f"{self.nom};{self.post_nom};{self.prenom};{self.adresse};{self.genre};{self.age_en_mois};{self.age_en_annees};{self.code}"
        encrypted_info = self.encrypt(patient_info, self.secret_key)

        # Générer le QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(encrypted_info)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        # Sauvegarder le QR code dans le champ ImageField
        qr_code_name = f"qr_code_{self.code}.png"
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        self.qr_code.save(qr_code_name, ContentFile(buffer.getvalue()), save=False)

        # Appeler la méthode save du parent pour sauvegarder l'objet dans la base de données
        super().save(*args, **kwargs)

    def encrypt(self, text, key):
        fernet = Fernet(base64.urlsafe_b64decode(key))
        encrypted = fernet.encrypt(text.encode())
        return encrypted.decode()

    def decrypt(self, encrypted_text, key):
        fernet = Fernet(base64.urlsafe_b64decode(key))
        decrypted = fernet.decrypt(encrypted_text.encode())
        return decrypted.decode()

    def __str__(self):
        return self.code



class VisitePatient(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    clinical = models.ForeignKey(Clinical,on_delete=models.CASCADE)
    date_visite = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.patient)



class SSI(models.Model):
    patient = models.OneToOneField('Patient', on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tension = models.CharField(max_length=20, blank=True)
    poids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)
    date_register = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.patient)




@receiver(pre_save, sender=Patient)
def patient_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.code:
        try:
            existing_patient = Patient.objects.get(code=instance.code)
            instance.id = existing_patient.id  # Utiliser l'ID de l'existant pour mise à jour
            instance.date_register = existing_patient.date_register  # Conserver la date d'enregistrement initiale
        except Patient.DoesNotExist:
            pass
    else:
        instance.code = str(uuid.uuid4()).replace('-', '').upper()[:10]




@receiver(post_save, sender=VisitePatient)
def create_ssi_for_visite(sender, instance, created, **kwargs):
    if created:
        SSI.objects.get_or_create(patient=instance.patient, clinical=instance.clinical)


# Ajouter des signaux pour la création de VisitePatient si le patient n'existe pas encore
@receiver(post_save, sender=Patient)
def create_visite_patient(sender, instance, created, **kwargs):
    if created:
        VisitePatient.objects.get_or_create(patient=instance, clinical=instance.clinical)