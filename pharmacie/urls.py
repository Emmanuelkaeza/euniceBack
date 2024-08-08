from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategorieMedicamentViewSet, GestionStockViewSet, VenteViewSet,MedicamentViewSet

router = DefaultRouter()
router.register(r'categories', CategorieMedicamentViewSet)
router.register(r'medicament', MedicamentViewSet)
router.register(r'stocks', GestionStockViewSet)
router.register(r'ventes', VenteViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
