from django.contrib import admin
from .models import DossierEnvoi

class DossierEnvoiAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender_clinical', 'receiver_clinical', 'date_sent', 'status')
    list_filter = ('sender_clinical', 'receiver_clinical', 'status', 'date_sent')
    search_fields = ('sender_clinical__nom', 'receiver_clinical__nom', 'patient__nom', 'patient__post_nom', 'patient__prenom')
    ordering = ('-date_sent',)

admin.site.register(DossierEnvoi, DossierEnvoiAdmin)
