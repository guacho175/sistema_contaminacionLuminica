from django.db import models
from django.utils import timezone
from .choices import tipo_alumbrado
from usuarios.models import Persona

# Create your models here.
class Titular(Persona):
    direccion = models.CharField(max_length=500, verbose_name='Dirección')

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.a_paterno, self.a_materno)
    
    class Meta:
        db_table = 'titular'
        verbose_name = 'Titular'
        verbose_name_plural = 'Titulares'


class RepresentanteLegal(Persona):
    direccion = models.CharField(max_length=500, verbose_name='Dirección')

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.a_paterno, self.a_materno)
    
    class Meta:
        db_table = 'representanteLegal'
        verbose_name = 'Representante legal'
        verbose_name_plural = 'Respresentantes legales'


class DetalleLuminaria(models.Model):
    cantidad = models.IntegerField(verbose_name='Cantidad')
    tipo_lampara = models.CharField(max_length=50, verbose_name='Tipo de lampara')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    potencia = models.FloatField(max_length=500, verbose_name='Potencia (W)')
    fecha_instalacion = models.DateField(verbose_name='Fecha de instalación')
    cod_certificacion = models.CharField(max_length=100, verbose_name='Código de certificación')
    fecha_certificacion = models.DateField(verbose_name='Fecha de certificación')

    def __str__(self):
        return "{}".format(self.cod_certificacion)
    
    class Meta:
        db_table = 'detalleLuminaria'
        verbose_name = 'Detalle luminaria'
        verbose_name_plural = 'Detalle luminarias'


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    latitud = models.FloatField(max_length=500, verbose_name='Latitud')
    longitud = models.FloatField(max_length=500, verbose_name='Longitud')
    tipo_alumbrado = models.CharField(max_length=1, choices=tipo_alumbrado, default='v', verbose_name='Tipo de alumbrado')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')
    creado = models.DateTimeField(default=timezone.now, editable=False)   
    # FK
    detalle_luminarias = models.ForeignKey(DetalleLuminaria, null=False, on_delete=models.RESTRICT)
    representante_legal = models.ForeignKey(RepresentanteLegal, null=False, on_delete=models.RESTRICT)
    titular = models.ForeignKey(Titular, null=False, on_delete=models.RESTRICT)

    def __str__(self):
        return "{}, tipo de alumbrado: {} ".format(self.nombre, self.get_tipo_alumbrado_display())
    
    class Meta:
        db_table = 'proyecto'
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'