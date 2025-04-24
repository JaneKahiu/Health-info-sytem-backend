from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import HealthProgram, Client
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
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'email']