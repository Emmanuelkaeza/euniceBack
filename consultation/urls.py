from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultationViewSet, MedicamentPrescritViewSet, ExamenDemandeViewSet

router = DefaultRouter()
router.register(r'consultations', ConsultationViewSet)
router.register(r'medicaments-prescrits', MedicamentPrescritViewSet)
router.register(r'examens-demandes', ExamenDemandeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
