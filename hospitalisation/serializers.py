from rest_framework import serializers
from .models import Hospitalisation, SuiviQuotidien, ExamenPostHospitalisation, MedicamentPostHospitalisation

class ExamenPostHospitalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenPostHospitalisation
        fields = '__all__'

class MedicamentPostHospitalisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicamentPostHospitalisation
        fields = '__all__'

class HospitalisationSerializer(serializers.ModelSerializer):
    examens_post_hospitalisation = ExamenPostHospitalisationSerializer(many=True, read_only=True)
    medicaments_post_hospitalisation = MedicamentPostHospitalisationSerializer(many=True, read_only=True)

    class Meta:
        model = Hospitalisation
        fields = '__all__'

class SuiviQuotidienSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuiviQuotidien
        fields = '__all__'
