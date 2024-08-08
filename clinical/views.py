from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import ZoneDeSante, AireDeSante, Clinical, Affectation ,Service
from .serializers import ZoneDeSanteSerializer, AireDeSanteSerializer, ClinicalSerializer, AffectationSerializer,ServiceSerializer

class ZoneDeSanteViewSet(viewsets.ModelViewSet):
    queryset = ZoneDeSante.objects.all()
    serializer_class = ZoneDeSanteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code_zone']
    ordering_fields = ['name', 'code_zone']

class AireDeSanteViewSet(viewsets.ModelViewSet):
    queryset = AireDeSante.objects.all()
    serializer_class = AireDeSanteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['health_zone']
    search_fields = ['name', 'health_zone__name']
    ordering_fields = ['name', 'health_zone']

class ClinicalViewSet(viewsets.ModelViewSet):
    queryset = Clinical.objects.all()
    serializer_class = ClinicalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['membership', 'category', 'aire_de_sante']
    search_fields = ['name', 'zip_cod', 'matricul']
    ordering_fields = ['name', 'matricul']

class AffectationViewSet(viewsets.ModelViewSet):
    queryset = Affectation.objects.all()
    serializer_class = AffectationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['clinical', 'email', 'poste', 'is_approuve', 'service'] 
    search_fields = ['clinical__name', 'email__username', 'poste','service__name']
    ordering_fields = ['date_register', 'poste']



class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name'] 
    search_fields = ['name']  
    ordering_fields = ['id', 'name'] 
