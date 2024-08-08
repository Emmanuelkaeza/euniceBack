from django.db import models
from django.conf import settings
from clinical.models import Clinical

class DossierEnvoi(models.Model):
    sender_clinical = models.ForeignKey(Clinical, related_name='sent_dossiers', on_delete=models.CASCADE)
    receiver_clinical = models.ForeignKey(Clinical, related_name='received_dossiers', on_delete=models.CASCADE)
    date_sent = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='dossiers/')
    status = models.CharField(max_length=20, choices=[('sent', 'Sent'), ('received', 'Received')], default='sent')

    def __str__(self):
        return f"Dossier de {self.patient.nom} envoyé de {self.sender_clinical.name} à {self.receiver_clinical.name}"
