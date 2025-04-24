from rest_framework import serializers
from .models import HealthProgram, Client

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    enrolled_program = HealthProgramSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = ['id', 'full_name', 'email', 'age', 'gender' ,'enrolled_program']