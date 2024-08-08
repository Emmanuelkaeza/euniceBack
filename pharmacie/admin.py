from django.contrib import admin
from .models import CategorieMedicament, GestionStock, Vente,Medicament

@admin.register(CategorieMedicament)
class CategorieMedicamentAdmin(admin.ModelAdmin):
    list_display = ['nom']
    search_fields = ['nom']

@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie']
    search_fields = ['nom', 'categorie__nom']

@admin.register(GestionStock)
class GestionStockAdmin(admin.ModelAdmin):
    list_display = ['medicament', 'quantite', 'date_entree', 'prix_unitaire', 'clinical']
    list_filter = ['date_entree', 'clinical']
    search_fields = ['medicament__nom', 'clinical__name']
@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ['medicament', 'quantite', 'date_vente', 'montant_total', 'clinical']
    list_filter = ['date_vente', 'clinical']
    search_fields = ['medicament__medicament', 'clinical__name']
