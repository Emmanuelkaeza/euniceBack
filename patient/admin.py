from django.contrib import admin
from .models import Patient, SSI,VisitePatient
from hospitalisation.models import Hospitalisation, SuiviQuotidien
from laboratoire.models import Laboratoire
from consultation.models import Consultation

class SSIInline(admin.StackedInline):
    model = SSI
    extra = 1

class HospitalisationInline(admin.StackedInline):
    model = Hospitalisation
    extra = 1

class SuiviQuotidienInline(admin.StackedInline):
    model = SuiviQuotidien
    extra = 1

class LaboratoireInline(admin.StackedInline):
    model = Laboratoire
    extra = 1

class ConsultationInline(admin.StackedInline):
    model = Consultation
    extra = 1

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['nom', 'post_nom', 'prenom', 'adresse', 'genre', 'date_birth', 'age_en_mois', 'age_en_annees', 'clinical', 'code', 'get_hospitalisations', 'get_suivis', 'get_laboratoires', 'get_consultations']
    search_fields = ['nom', 'post_nom', 'prenom', 'adresse', 'code']
    inlines = [SSIInline]

    def get_hospitalisations(self, obj):
        return ', '.join([str(h) for h in Hospitalisation.objects.filter(patient=obj)])
    get_hospitalisations.short_description = 'Hospitalisations'

    def get_suivis(self, obj):
        return ', '.join([str(s) for s in SuiviQuotidien.objects.filter(hospitalisation__patient=obj)])
    get_suivis.short_description = 'Suivis Quotidiens'

    def get_laboratoires(self, obj):
        return ', '.join([str(l) for l in Laboratoire.objects.filter(patient=obj)])
    get_laboratoires.short_description = 'Laboratoires'

    def get_consultations(self, obj):
        return ', '.join([str(c) for c in Consultation.objects.filter(patient=obj)])
    get_consultations.short_description = 'Consultations'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['hospitalisations'] = Hospitalisation.objects.all()
        extra_context['suivis'] = SuiviQuotidien.objects.all()
        extra_context['laboratoires'] = Laboratoire.objects.all()
        extra_context['consultations'] = Consultation.objects.all()
        return super(PatientAdmin, self).changelist_view(request, extra_context=extra_context)


@admin.register(SSI)
class SSIAdmin(admin.ModelAdmin):
    list_display = ['patient', 'temperature', 'tension', 'poids', 'clinical']
    list_filter = ['clinical']
    search_fields = ['patient__nom', 'patient__post_nom', 'patient__prenom']

@admin.register(VisitePatient)
class VisitePatientAdmin(admin.ModelAdmin):
    list_display = ('patient', 'clinical', 'date_visite')
    search_fields = ('patient__nom', 'patient__post_nom', 'patient__prenom', 'clinical__name')
    list_filter = ('date_visite', 'clinical')