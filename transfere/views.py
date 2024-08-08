from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import DossierEnvoi
from .serializers import DossierEnvoiSerializer

class DossierEnvoiViewSet(viewsets.ModelViewSet):
    queryset = DossierEnvoi.objects.all()
    serializer_class = DossierEnvoiSerializer
    #permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['sender_clinical', 'receiver_clinical', 'date_sent', 'status']
    search_fields = [ 'sender_clinical__nom', 'receiver_clinical__nom']
    ordering_fields = ['date_sent', 'status']

    #def get_queryset(self):
    #    user_clinical = self.request.user.clinical
    #    if self.action == 'list':
    #        return DossierEnvoi.objects.filter(receiver_clinical=user_clinical)
    #    return super().get_queryset()
