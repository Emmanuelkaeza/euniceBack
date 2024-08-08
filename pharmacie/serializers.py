from rest_framework import serializers
from .models import CategorieMedicament, GestionStock, Vente,Medicament

class CategorieMedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieMedicament
        fields = '__all__'

class GestionStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestionStock
        fields = '__all__'

class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = '__all__'


class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'