from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ZoneDeSanteViewSet, AireDeSanteViewSet, ClinicalViewSet, AffectationViewSet,ServiceViewSet

router = DefaultRouter()
router.register(r'zones', ZoneDeSanteViewSet)
router.register(r'aires', AireDeSanteViewSet)
router.register(r'clinicals', ClinicalViewSet)
router.register(r'affectations', AffectationViewSet)
router.register(r'services', ServiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
