from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, SSIViewSet, VisitePatientViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'visitepatient', VisitePatientViewSet)
router.register(r'ssi', SSIViewSet)
#router.register(r'patients-with-empreintes', PatientWithEmpreintesViewSet, basename='patient-with-empreintes')

urlpatterns = [
    path('', include(router.urls)),
    # Ajout de l'URL pour la génération du PDF
    path('patients/<int:pk>/generate-pdf/', PatientViewSet.as_view({'get': 'generate_pdf'}), name='generate-pdf'),
]
