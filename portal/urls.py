from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'healthprograms', HealthProgramViewSet, basename='healthprogram')
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),

    path('home/', home, name='home'),
]
