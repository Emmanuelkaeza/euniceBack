from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HospitalisationViewSet, SuiviQuotidienViewSet, ExamenPostHospitalisationViewSet, MedicamentPostHospitalisationViewSet

router = DefaultRouter()
router.register(r'hospitalisations', HospitalisationViewSet)
router.register(r'suivis', SuiviQuotidienViewSet)
router.register(r'examen-post-hospitalisation', ExamenPostHospitalisationViewSet)
router.register(r'medicament-post-hospitalisation', MedicamentPostHospitalisationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
