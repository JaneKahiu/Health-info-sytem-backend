from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'healthprograms', HealthProgramViewSet, basename='healthprogram')

urlpatterns = [
    path('api/', include(router.urls)),
    path("", home ,name='home'),
]