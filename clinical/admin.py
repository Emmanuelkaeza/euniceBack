from django.contrib import admin
from .models import ZoneDeSante, AireDeSante, Clinical, Affectation,Service
from patient.models import Patient

class PatientInline(admin.TabularInline):
    model = Patient
    extra = 0
    fields = ['nom', 'post_nom', 'prenom', 'adresse', 'genre', 'type_patient', 'age_en_mois', 'age_en_annees', 'code']

@admin.register(ZoneDeSante)
class ZoneDeSanteAdmin(admin.ModelAdmin):
    list_display = ['name', 'code_zone', 'creation_date']
    search_fields = ['name', 'code_zone']

@admin.register(AireDeSante)
class AireDeSanteAdmin(admin.ModelAdmin):
    list_display = ['name', 'health_zone', 'creation_date']
    search_fields = ['name', 'health_zone__name']

@admin.register(Clinical)
class ClinicalAdmin(admin.ModelAdmin):
    list_display = ['name', 'membership', 'category', 'aire_de_sante', 'zip_cod', 'matricul', 'creation_date']
    search_fields = ['name', 'membership', 'category', 'aire_de_sante__name', 'zip_cod', 'matricul']
    inlines = [PatientInline]

@admin.register(Affectation)
class AffectationAdmin(admin.ModelAdmin):
    list_display = ['clinical', 'email', 'poste', 'date_register', 'is_approuve']
    search_fields = ['clinical__name', 'email__username', 'poste','service__name']
    list_filter = ['poste', 'is_approuve']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)