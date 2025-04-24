from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import HealthProgram, Client
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import HealthProgramSerializer, ClientSerializer

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
@api_view(['GET'])
def home(request):
    return HttpResponse("Hello, Django!")

class HealthProgramViewSet(viewsets.ModelViewSet):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['age', 'enrolled_program']  
    search_fields = ['full_name', 'enrolled_program__name']  
