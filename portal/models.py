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
