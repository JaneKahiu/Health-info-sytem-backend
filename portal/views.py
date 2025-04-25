from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import HealthProgram, Client, Notification
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import HealthProgramSerializer, ClientSerializer, NotificationSerializer
from .notification_utils import create_client_notification
from .notification_utils import create_program_notification

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
@api_view(['GET'])
def home(request):
    return HttpResponse("Hello, Django!")

class HealthProgramViewSet(viewsets.ModelViewSet):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer

def perform_update(self, serializer):
    program = serializer.save()
    create_program_notification(program, "updated")

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().prefetch_related('enrolled_program')
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['age', 'enrolled_program']  
    search_fields = ['full_name', 'enrolled_program__name']

def perform_create(self, serializer):
    client = serializer.save()
    create_client_notification(client, "enrolled")

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer
    
    def get_queryset(self):
        """Filter notifications for the current user if authenticated"""
        queryset = Notification.objects.all().order_by('-created_at')
        if self.request.user.is_authenticated:
            queryset = queryset.filter(recipient=self.request.user)
        return queryset
    
    @action(detail=False, methods=['post'])
    def mark_as_read(self, request):
        """Mark notifications as read"""
        notification_ids = request.data.get('notification_ids', [])
        if notification_ids:
            Notification.objects.filter(id__in=notification_ids).update(is_read=True)
        return Response({'status': 'Notifications marked as read'})
    
    @action(detail=False, methods=['get'])
    def unread_count(self, request):
        """Get count of unread notifications"""
        count = self.get_queryset().filter(is_read=False).count()
        return Response({'count': count})