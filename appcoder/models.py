from django.db import models

# Create your models here.

class Usuarios (models.Model):
    nombre = models.CharField(max_length=30),
    edad = models.IntegerField(),
    fecha_nacimiento = models.DateField(null=True)
    