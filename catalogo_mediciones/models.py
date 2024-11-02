from django.db import models
from django.utils import timezone
from .choices import cumplimiento, tipo_instrumento
from proyectos.models import Proyecto
from inspectores.models import Inspector

class InstrumentoMedicion(models.Model):
    tipo = models.CharField(max_length=1, choices=tipo_instrumento, verbose_name='Iipo')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    num_serie = models.CharField(max_length=50, verbose_name='N° de Serie')
    
    def __str__(self):
        return "{} {}".format(self.tipo, self.num_serie)
        
    class Meta:
        db_table = 'instrumento_medicion'
        verbose_name = 'Instrumento de medición'
        verbose_name_plural = 'Instrumentos de medición'


class DetalleMedicion(models.Model):
    longitud = models.FloatField(verbose_name='Longitud')
    latitud = models.FloatField(verbose_name='Latitud')
    temperatura = models.FloatField(verbose_name='Temperatura (°C)')
    humedad = models.FloatField(verbose_name='Humedad (%)')
    valor_medido = models.FloatField(verbose_name='Valor medido')
    instrumento_medicion = models.ForeignKey(InstrumentoMedicion, null=False, on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now, editable=False)    


class Medicion(models.Model):
    cumplimiento = models.CharField(max_length=1, choices=cumplimiento, blank=True, null=True, verbose_name='Cumplimiento')
    inspector = models.ForeignKey(Inspector, null=False, on_delete=models.RESTRICT)
    proyecto = models.ForeignKey(Proyecto, null=False, on_delete=models.RESTRICT)
    detalleMedicion = models.ForeignKey(DetalleMedicion, null=True, blank=True, on_delete=models.RESTRICT)