from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LaboratoireViewSet

router = DefaultRouter()
router.register(r'laboratoires', LaboratoireViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
