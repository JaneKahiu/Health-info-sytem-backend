from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import CustomUser
from rest_framework import serializers
from rest_framework.exceptions import ValidationError



class CustomUserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'username', 'password', 'password2')

    def validate(self, attrs):
        
        return attrs
