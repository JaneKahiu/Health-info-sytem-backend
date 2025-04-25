from django.db import models

# Create your models here.
class HealthProgram(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description =models.TextField()

    def __str__(self):
        return self.name

from django.db import models

class Client(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='other')
    enrolled_program = models.ManyToManyField('HealthProgram', related_name='clients')

    def __str__(self):
        return self.full_name

from django.db import models
from django.conf import settings

class Notification(models.Model):
    # If you have User model for doctors/staff
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications',
        null=True,
        blank=True
    )
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    related_client = models.ForeignKey(
        'Client',  
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )
    related_program = models.ForeignKey(
        'HealthProgram',  
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.message
