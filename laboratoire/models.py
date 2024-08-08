from django.db import models
from patient.models import Patient
from clinical.models import Clinical
# Create your models here.

class Laboratoire(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_examen = models.DateField(auto_now_add=True)
    type_examen = models.CharField(max_length=100)
    resultat = models.TextField()
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)
    date_register = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.patient)
