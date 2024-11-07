from django.db import models
from django.utils import timezone
from .choices import cumplimiento, tipo_instrumento
from inspectores.models import Inspector
from proyectos.models import Proyecto

class InstrumentoMedicion(models.Model):
    tipo = models.CharField(max_length=1, choices=tipo_instrumento, verbose_name='Iipo')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    num_serie = models.CharField(max_length=50, verbose_name='N° de Serie')
    
    def __str__(self):
        return "{}".format(self.get_tipo_display())
        
    class Meta:
        db_table = 'instrumento_medicion'
        verbose_name = 'Instrumento de medición'
        verbose_name_plural = 'Instrumentos de medición'


class Medicion(models.Model):
    cumplimiento = models.CharField(max_length=1, choices=cumplimiento, blank=True, null=True, verbose_name='Cumplimiento')
    latitud = models.FloatField(verbose_name='Latitud')
    longitud = models.FloatField(verbose_name='Longitud')
    temperatura = models.FloatField(verbose_name='Temperatura (°C)')
    humedad = models.FloatField(verbose_name='Humedad (%)')
    valor_medido = models.FloatField(verbose_name='Valor medido')
    observacion = models.CharField(max_length=500, verbose_name='Observación')
    inspector = models.ForeignKey(Inspector, null=False, on_delete=models.RESTRICT)
    instrumento_medicion = models.ForeignKey(InstrumentoMedicion, null=False, on_delete=models.RESTRICT)
    proyecto = models.ForeignKey(Proyecto, null=False, on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now, editable=False)  
    
    def __str__(self):
        return "{} {}".format(self.latitud, self.longitud)
        
    class Meta:
        db_table = 'medicion'
        verbose_name = 'Medición'
        verbose_name_plural = 'Mediciones'

