from django.db import models

# Create your models here.
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField(default=0.0)

class Vehiculo(Persona, models.Model):
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.IntegerField()
    

class Mascota (Vehiculo, models.Model):
    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)