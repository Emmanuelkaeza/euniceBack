from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  DossierEnvoiViewSet

router = DefaultRouter()
router.register(r'dossier-envois', DossierEnvoiViewSet, basename='dossier-envoi')

urlpatterns = [
    path('', include(router.urls)),
]
