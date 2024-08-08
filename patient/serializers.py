from rest_framework import serializers
from .models import Patient, SSI,VisitePatient
from django.conf import settings
from django.urls import reverse

class SSISerializer(serializers.ModelSerializer):
    class Meta:
        model = SSI
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    ssi = SSISerializer(read_only=True)
    pdf_url = serializers.SerializerMethodField()

    
    class Meta:
        model = Patient
        fields = '__all__'

    def get_pdf_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(reverse('generate-pdf', kwargs={'pk': obj.pk}))
        return None

class VisitePatientSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    clinical = serializers.StringRelatedField()

    class Meta :
        model= VisitePatient
        fields ='__all__'
