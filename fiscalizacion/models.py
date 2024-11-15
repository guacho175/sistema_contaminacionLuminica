from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from proyectos.models import Proyecto

# Create your models here.

class Fiscalizacion(models.Model):
    temperatura = models.FloatField(blank=True, null=True, verbose_name='Temperatura (°C)')
    humedad = models.FloatField(blank=True, null=True, verbose_name='Humedad (%)')
    nivel_cumplimiento = models.FloatField(blank=True, null=True, verbose_name='Cumplimiento (%)')
    #FK
    proyecto = models.ForeignKey(Proyecto, null=False, on_delete=models.RESTRICT)
    usuario = models.ForeignKey(Usuario, null=False, on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now, editable=False)  


    def __str__(self):
        return "{}, {} {}".format(self.proyecto.nombre, self.usuario.nombre, self.usuario.a_materno)
        
    class Meta:
        db_table = 'fiscalizacion'
        verbose_name = 'Fiscalización'
        verbose_name_plural = 'Fiscalizaciones'


class Reporte(models.Model):
    creado = models.DateTimeField(default=timezone.now, editable=False)
    fiscalizacion = models.ForeignKey(Fiscalizacion, null=False, on_delete=models.RESTRICT)

    def __str__(self):
        return "{} ,{}".format(self.fiscalizacion.proyecto.nombre, self.creado)
        
    class Meta:
        db_table = 'reporte'
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'