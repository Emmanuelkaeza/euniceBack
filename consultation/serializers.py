from rest_framework import serializers
from .models import Consultation, MedicamentPrescrit, ExamenDemande

class MedicamentPrescritSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicamentPrescrit
        fields = '__all__'  

class ExamenDemandeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamenDemande
        fields = '__all__'  

class ConsultationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Consultation
        fields = '__all__'  

    