from django.contrib import admin
from .models import Laboratoire

@admin.register(Laboratoire)
class LaboratoireAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date_examen', 'type_examen', 'resultat', 'clinical']
    list_filter = ['patient', 'date_examen', 'type_examen', 'clinical']
    search_fields = ['patient__nom', 'patient__post_nom', 'patient__prenom', 'type_examen', 'resultat']
