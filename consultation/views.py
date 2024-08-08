from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Consultation, MedicamentPrescrit, ExamenDemande
from .serializers import ConsultationSerializer, MedicamentPrescritSerializer, ExamenDemandeSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['patient', 'date_consultation', 'clinical', 'is_hospitaliser']
    search_fields = ['patient__nom', 'patient__post_nom', 'patient__prenom', 'symptomes', 'diagnostic', 'recommandations']
    ordering_fields = ['date_consultation', 'is_hospitaliser']

class MedicamentPrescritViewSet(viewsets.ModelViewSet):
    queryset = MedicamentPrescrit.objects.all()
    serializer_class = MedicamentPrescritSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['consultation', 'nom', 'dosage', 'frequence', 'duree', 'date_jour','clinical']
    search_fields = ['nom', 'dosage', 'frequence', 'duree']
    ordering_fields = ['nom', 'dosage', 'frequence', 'duree', 'date_jour']  

class ExamenDemandeViewSet(viewsets.ModelViewSet):
    queryset = ExamenDemande.objects.all()
    serializer_class = ExamenDemandeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['consultation', 'type_examen', 'description', 'date_jour','clinical']
    search_fields = ['type_examen', 'description']
    ordering_fields = ['type_examen', 'description', 'date_jour']  
