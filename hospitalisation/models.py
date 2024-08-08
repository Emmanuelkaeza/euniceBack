from django.db import models
from patient.models import Patient
from clinical.models import Clinical
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.
class Hospitalisation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_admission = models.DateTimeField(default=timezone.now)
    date_sortie = models.DateField(blank=True, null=True)
    motif_admission = models.TextField()
    diagnostic_final = models.TextField(blank=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.patient)

class SuiviQuotidien(models.Model):
    hospitalisation = models.ForeignKey(Hospitalisation, on_delete=models.CASCADE)
    date_suivi = models.DateTimeField(default=timezone.now)
    symptomes = models.TextField()
    evolution = models.TextField()
    traitement_administre = models.TextField(blank=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.hospitalisation)

    def save(self, *args, **kwargs):
        if self.hospitalisation.date_sortie is not None:
            raise ValidationError("Vous ne pouvez pas ajouter un suivi quotidien après la date de sortie.")
        super(SuiviQuotidien, self).save(*args, **kwargs)


class ExamenPostHospitalisation(models.Model):
    hospitalisation = models.ForeignKey(Hospitalisation, on_delete=models.CASCADE)
    type_examen = models.CharField(max_length=255)
    date_examen = models.DateField()
    day_date = models.DateField(auto_now_add=True)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.type_examen} - {self.date_examen}"

class MedicamentPostHospitalisation(models.Model):
    hospitalisation = models.ForeignKey(Hospitalisation, on_delete=models.CASCADE)
    nom_medicament = models.CharField(max_length=255)
    posologie = models.CharField(max_length=255)
    duree = models.CharField(max_length=255)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)
    day_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom_medicament