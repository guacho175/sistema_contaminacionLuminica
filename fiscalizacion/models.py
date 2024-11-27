from django.db import models
from django.utils import timezone
from proyectos.models import Proyecto
from django.contrib.auth.models import User as Usuario


class Fiscalizacion(models.Model):
    #FK
    proyecto = models.ForeignKey(Proyecto, null=False, on_delete=models.RESTRICT)
    usuario = models.ForeignKey(Usuario, null=False, on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now, editable=False)  

    def __str__(self):
        return "cod: {} - {} ".format(self.id, self.proyecto.nombre) 
        
    class Meta:
        db_table = 'fiscalizacion'
        verbose_name = 'Fiscalización'
        verbose_name_plural = 'Fiscalizaciones'


class Reporte(models.Model):
    fiscalizacion = models.ForeignKey(Fiscalizacion, null=False, on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "{} ,{}".format(self.fiscalizacion.proyecto.nombre, self.creado)
        
    class Meta:
        db_table = 'reporte'
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'