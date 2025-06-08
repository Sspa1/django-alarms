from django.db import models

# Create your models here.
class Alarma(models.Model):
    nombre_estacion = models.CharField(max_length=150)
    tipo_estacion = models.CharField(max_length=150)
    tech_area = models.CharField(max_length=150)
    activa = models.BooleanField(default=False)