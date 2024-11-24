from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from proyectos.models import Proyecto
from services.utils.GenerarNombre import GenerarNombre


class Fiscalizacion(models.Model):
    foto = models.ImageField(upload_to=GenerarNombre.generar_nombre_medicion, null=True, default='medicion/medicion.png')
    #FK
    proyecto = models.ForeignKey(Proyecto, null=False, on_delete=models.RESTRICT)
    usuario = models.ForeignKey(Usuario, null=False, on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now, editable=False)  

    def __str__(self):
        return "cod: {} - {} - {} {}".format(self.id, self.proyecto.nombre, self.usuario.nombre, self.usuario.a_materno)
        
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