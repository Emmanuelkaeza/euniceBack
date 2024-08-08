from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Hospitalisation, SuiviQuotidien, ExamenPostHospitalisation, MedicamentPostHospitalisation
from .serializers import HospitalisationSerializer, SuiviQuotidienSerializer, ExamenPostHospitalisationSerializer, MedicamentPostHospitalisationSerializer

class HospitalisationFilter(filters.FilterSet):
    patient = filters.NumberFilter(field_name="patient")
    date_admission = filters.DateFilter(field_name="date_admission")
    date_sortie = filters.DateFilter(field_name="date_sortie")
    clinical = filters.NumberFilter(field_name="clinical")

    class Meta:
        model = Hospitalisation
        fields = ['patient', 'date_admission', 'date_sortie', 'clinical']

class SuiviQuotidienFilter(filters.FilterSet):
    hospitalisation = filters.NumberFilter(field_name="hospitalisation__id")
    date_suivi = filters.DateFilter(field_name="date_suivi")
    traitement_administre = filters.CharFilter(field_name="traitement_administre", lookup_expr='icontains')
    clinical = filters.NumberFilter(field_name="clinical")

    class Meta:
        model = SuiviQuotidien
        fields = ['hospitalisation', 'date_suivi', 'traitement_administre', 'clinical']

class ExamenPostHospitalisationFilter(filters.FilterSet):
    hospitalisation = filters.NumberFilter(field_name="hospitalisation__id")
    date_examen = filters.DateFilter(field_name="date_examen")
    clinical = filters.NumberFilter(field_name="clinical")

    class Meta:
        model = ExamenPostHospitalisation
        fields = ['hospitalisation', 'date_examen', 'clinical']

class MedicamentPostHospitalisationFilter(filters.FilterSet):
    hospitalisation = filters.NumberFilter(field_name="hospitalisation__id")
    clinical = filters.NumberFilter(field_name="clinical")

    class Meta:
        model = MedicamentPostHospitalisation
        fields = ['hospitalisation', 'clinical']

class HospitalisationViewSet(viewsets.ModelViewSet):
    queryset = Hospitalisation.objects.all()
    serializer_class = HospitalisationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HospitalisationFilter

class SuiviQuotidienViewSet(viewsets.ModelViewSet):
    queryset = SuiviQuotidien.objects.all()
    serializer_class = SuiviQuotidienSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SuiviQuotidienFilter

class ExamenPostHospitalisationViewSet(viewsets.ModelViewSet):
    queryset = ExamenPostHospitalisation.objects.all()
    serializer_class = ExamenPostHospitalisationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExamenPostHospitalisationFilter

class MedicamentPostHospitalisationViewSet(viewsets.ModelViewSet):
    queryset = MedicamentPostHospitalisation.objects.all()
    serializer_class = MedicamentPostHospitalisationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MedicamentPostHospitalisationFilter
