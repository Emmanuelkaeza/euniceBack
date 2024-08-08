from rest_framework import serializers
from .models import ZoneDeSante, AireDeSante, Clinical, Affectation,Service

class ZoneDeSanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoneDeSante
        fields = '__all__'

class AireDeSanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AireDeSante
        fields = '__all__'

class ClinicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinical
        fields = '__all__'

class AffectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affectation
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'