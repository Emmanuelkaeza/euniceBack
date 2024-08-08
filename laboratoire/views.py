from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Laboratoire
from .serializers import LaboratoireSerializer

class LaboratoireViewSet(viewsets.ModelViewSet):
    queryset = Laboratoire.objects.all()
    serializer_class = LaboratoireSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['patient', 'date_examen', 'type_examen', 'clinical']
    search_fields = ['patient__nom', 'patient__post_nom', 'patient__prenom', 'type_examen', 'resultat']
    ordering_fields = ['date_examen', 'type_examen']
