from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre sensor')
    address = models.CharField(max_length=250, verbose_name='Dirección')
    lat = models.FloatField(verbose_name='Latitud')
    lng = models.FloatField(verbose_name='Longitud')
    cumpl = models.IntegerField(default=0, verbose_name='Nivel Cumplimiento')

    class Meta:
        verbose_name = "Sensor"
        verbose_name_plural = "Sensores"
        ordering = ['name']

    def __str__(self):
        return self.name
