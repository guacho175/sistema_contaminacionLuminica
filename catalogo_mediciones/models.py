from django.db import models
from django.utils import timezone

# Create your models here.
class tipo_alumbrado_art5(models.Model):
    direccion = models.CharField(max_length=250, verbose_name='Ubicación')
    latitud = models.FloatField(verbose_name='Latitud')
    longitud = models.FloatField(verbose_name='Longitud')
    creado = models.DateTimeField(default=timezone.now)
    menor_igual_90grados = models.FloatField(verbose_name='Intensidad Luminosa <= 90º')
    mayor_90grados = models.FloatField(verbose_name='Intensidad Luminosa > 90º')
    clase_luminaria = models.CharField(max_length=50, verbose_name='Clase de luminaria')
    emision_reflexion =  models.FloatField(verbose_name='Emisión por Reflexión')
    proteccion_especial = models.CharField(max_length=2, verbose_name='Área de protección especial')
    radiancia_espectral = models.FloatField(verbose_name='Radiancia Espectral')
    emision_conjunta = models.CharField(max_length=2, verbose_name='Emision conjunta considerada')
    Observaciones = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observaciones')
    
    class Meta:
        verbose_name = 'Medicion_art5'
        verbose_name_plural = 'Mediciones_art5'

    def __str__(self):
        return self.address
