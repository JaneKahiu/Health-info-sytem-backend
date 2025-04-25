from rest_framework import serializers
from .models import HealthProgram, Client, Notification

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    enrolled_program = HealthProgramSerializer(many=True, read_only=True)
    program_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Client
        fields = ['id', 'full_name', 'email', 'age', 'gender', 'enrolled_program', 'program_ids']
    
    def create(self, validated_data):
        program_ids = validated_data.pop('program_ids', [])
        client = Client.objects.create(**validated_data)
        
        if program_ids:
            for program_id in program_ids:
                client.enrolled_program.add(program_id)
        
        return client
    
    def update(self, instance, validated_data):
        program_ids = validated_data.pop('program_ids', None)
        
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        
        if program_ids is not None:
            instance.enrolled_program.clear()
            for program_id in program_ids:
                instance.enrolled_program.add(program_id)
        
        return instance
    
class NotificationSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    
    class Meta:
        model = Notification
        fields = ['id', 'message', 'is_read', 'date', 'related_client', 'related_program']
        
    def get_date(self, obj):
        return obj.created_at.strftime('%Y-%m-%d')