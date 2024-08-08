from django.contrib import admin
from .models import Consultation, MedicamentPrescrit, ExamenDemande

class MedicamentPrescritInline(admin.TabularInline):
    model = MedicamentPrescrit
    extra = 1

class ExamenDemandeInline(admin.TabularInline):
    model = ExamenDemande
    extra = 1

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    inlines = [MedicamentPrescritInline, ExamenDemandeInline]
    list_display = ('patient', 'date_consultation', 'clinical', 'is_hospitaliser')
    search_fields = ('patient__nom', 'patient__post_nom', 'clinical__name')
    list_filter = ('date_consultation', 'clinical')

admin.site.register(MedicamentPrescrit)
admin.site.register(ExamenDemande)
