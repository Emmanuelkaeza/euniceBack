from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import CategorieMedicament, GestionStock, Vente ,Medicament
from .serializers import CategorieMedicamentSerializer, GestionStockSerializer, VenteSerializer,MedicamentSerializer

class CategorieMedicamentViewSet(viewsets.ModelViewSet):
    queryset = CategorieMedicament.objects.all()
    serializer_class = CategorieMedicamentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom','clinical__name']
    ordering_fields = ['nom']

class MedicamentViewSet(viewsets.ModelViewSet):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom','clinical__name']
    ordering_fields = ['nom']

class GestionStockViewSet(viewsets.ModelViewSet):
    queryset = GestionStock.objects.all()
    serializer_class = GestionStockSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['medicament', 'date_entree', 'clinical']
    search_fields = ['medicament__nom', 'clinical__name']
    ordering_fields = ['date_entree', 'medicament']

class VenteViewSet(viewsets.ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['medicament', 'date_vente', 'clinical']
    search_fields = ['medicament__medicament', 'clinical__name']
    ordering_fields = ['date_vente', 'montant_total']