from rest_framework import serializers
from .models import  DossierEnvoi


class DossierEnvoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DossierEnvoi
        fields = '__all__'
