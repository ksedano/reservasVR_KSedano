from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    clase = models.CharField(max_length=100)

class Aula(models.Model):
	nombre = models.CharField(max_length=100)
	num_gafas = models.IntegerField(default=0)
	aforo = models.IntegerField(default=0)

class Reserva(models.Model):
	nombre = models.ForeignKey(User, on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	num_personas = models.IntegerField(default=0)
	num_gafas = models.IntegerField(default=0)
	aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
	fecha_hora = models.DateTimeField(default=timezone.now)
	fecha_inicio = models.DateTimeField(default=timezone.now)
	fecha_fin = models.DateTimeField(default=timezone.now)

class Gafa(models.Model):
	nombre = models.CharField(max_length=100)
	aula = models.ForeignKey(Aula, on_delete=models.CASCADE)