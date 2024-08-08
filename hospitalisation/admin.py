from django.contrib import admin
from .models import Hospitalisation, SuiviQuotidien, ExamenPostHospitalisation, MedicamentPostHospitalisation

class SuiviQuotidienInline(admin.TabularInline):
    model = SuiviQuotidien
    extra = 1

    def has_add_permission(self, request, obj=None):
        if obj and obj.date_sortie:
            return False
        return super().has_add_permission(request, obj)

class ExamenPostHospitalisationInline(admin.TabularInline):
    model = ExamenPostHospitalisation
    extra = 1

class MedicamentPostHospitalisationInline(admin.TabularInline):
    model = MedicamentPostHospitalisation
    extra = 1

@admin.register(Hospitalisation)
class HospitalisationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date_admission', 'date_sortie', 'motif_admission', 'diagnostic_final', 'clinical']
    list_filter = ['patient', 'date_admission', 'date_sortie', 'clinical']
    search_fields = ['patient__nom', 'patient__post_nom', 'patient__prenom', 'motif_admission', 'diagnostic_final']
    inlines = [SuiviQuotidienInline, ExamenPostHospitalisationInline, MedicamentPostHospitalisationInline]

@admin.register(SuiviQuotidien)
class SuiviQuotidienAdmin(admin.ModelAdmin):
    list_display = ['hospitalisation', 'date_suivi', 'symptomes', 'evolution', 'traitement_administre', 'clinical']
    list_filter = ['hospitalisation', 'date_suivi', 'traitement_administre', 'clinical']
    search_fields = ['hospitalisation__patient__nom', 'hospitalisation__patient__post_nom', 'hospitalisation__patient__prenom', 'symptomes', 'evolution', 'traitement_administre']

@admin.register(ExamenPostHospitalisation)
class ExamenPostHospitalisationAdmin(admin.ModelAdmin):
    list_display = ['hospitalisation', 'type_examen', 'date_examen', 'clinical', 'day_date']
    list_filter = ['hospitalisation', 'type_examen', 'date_examen', 'clinical', 'day_date']
    search_fields = ['hospitalisation__patient__nom', 'hospitalisation__patient__post_nom', 'hospitalisation__patient__prenom', 'type_examen']

@admin.register(MedicamentPostHospitalisation)
class MedicamentPostHospitalisationAdmin(admin.ModelAdmin):
    list_display = ['hospitalisation', 'nom_medicament', 'posologie', 'duree', 'clinical', 'day_date']
    list_filter = ['hospitalisation', 'nom_medicament', 'posologie', 'duree', 'clinical', 'day_date']
    search_fields = ['hospitalisation__patient__nom', 'hospitalisation__patient__post_nom', 'hospitalisation__patient__prenom', 'nom_medicament']
