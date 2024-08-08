from django.db import models
from patient.models import Patient
from clinical.models import Clinical
from hospitalisation.models import Hospitalisation
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_consultation = models.DateTimeField(default=timezone.now)
    symptomes = models.TextField()
    diagnostic = models.TextField()
    recommandations = models.TextField(blank=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)
    is_hospitaliser = models.BooleanField(default=False)

    def __str__(self):
        return f"Consultation of {self.patient} on {self.date_consultation}"

class MedicamentPrescrit(models.Model):
    consultation = models.ForeignKey(Consultation, related_name='medicaments_prescrits', on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    frequence = models.CharField(max_length=255)
    duree = models.CharField(max_length=255)
    date_jour = models.DateField(auto_now_add=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} for {self.consultation}"

class ExamenDemande(models.Model):
    consultation = models.ForeignKey(Consultation, related_name='examens_demandes', on_delete=models.CASCADE)
    type_examen = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_jour = models.DateField(auto_now_add=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.type_examen} for {self.consultation}"

@receiver(post_save, sender=Consultation)
def create_hospitalisation(sender, instance, created, **kwargs):
    if created and instance.is_hospitaliser:
        # Créer l'hospitalisation avec les détails nécessaires
        hospitalisation = Hospitalisation.objects.create(
            patient=instance.patient,
            motif_admission=instance.recommandations if instance.recommandations else 'Motif non spécifié',
            clinical=instance.clinical
        )
        # Mettre à jour la consultation avec l'hospitalisation créée
        instance.hospitalisation = hospitalisation
        instance.save()
