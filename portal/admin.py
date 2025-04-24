from django.contrib import admin
from .models import HealthProgram, Client

# Register your models here.
admin.site.register(HealthProgram)
admin.site.register(Client)