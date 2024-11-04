from django.db import models
from django.utils import timezone
from .choices import tipo_alumbrado, nivel_cumplimiento
from catalogo_mediciones.models import Medicion

# Create your models here.
class Titular(models.Model):
    run = models.CharField(max_length=15, verbose_name='Run')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    a_paterno = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    a_materno = models.CharField(max_length=50, verbose_name='Apellido Materno')
    direccon = models.CharField(max_length=500, verbose_name='Dirección')
    correo = models.CharField(max_length=100, verbose_name='Correo')
    creado = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.a_paterno, self.a_materno)
    
    class Meta:
        db_table = 'titular'
        verbose_name = 'Titular'
        verbose_name_plural = 'Titulares'


class RepresentanteLegal(models.Model):
    run = models.CharField(max_length=15, verbose_name='Run')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    a_paterno = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    a_materno = models.CharField(max_length=50, verbose_name='Apellido Materno')
    direccon = models.CharField(max_length=500, verbose_name='Dirección')
    correo = models.CharField(max_length=100, verbose_name='Correo')
    creado = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.a_paterno, self.a_materno)
    
    class Meta:
        db_table = 'representante_legal'
        verbose_name = 'Representante legal'
        verbose_name_plural = 'Respresentantes legales'


class DetalleLuminarias(models.Model):
    cantidad = models.IntegerField(verbose_name='Cantidad')
    tipo_lampara = models.CharField(max_length=50, verbose_name='Tipo de lampara')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    potencia = models.FloatField(max_length=500, verbose_name='Potencia (W)')
    fecha_instalacion = models.DateField(verbose_name='Fecha de instalación')
    cod_certificacion = models.CharField(max_length=100, verbose_name='Código de certificación')
    fecha_certificacion = models.DateField(verbose_name='Fecha de certificación')
    creado = models.DateTimeField(default=timezone.now, editable=False)    

    def __str__(self):
        return "{}".format(self.cod_certificacion)
    
    class Meta:
        db_table = 'detalle_luminarias'
        verbose_name = 'Detalle luminaria'
        verbose_name_plural = 'Detalle luminarias'


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    longitud = models.FloatField(max_length=500, verbose_name='Longitud')
    latitud = models.FloatField(max_length=500, verbose_name='Latitud')
    tipo_alumbrado = models.CharField(max_length=1, choices=tipo_alumbrado, default='v', verbose_name='Tipo de alumbrado')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')
    nv_cumplimiento = models.CharField(max_length=1, choices=nivel_cumplimiento,default='0', verbose_name='Nivel de cumplimiento')
    titular = models.ForeignKey(Titular, null=False, on_delete=models.RESTRICT)
    representante_legal = models.ForeignKey(RepresentanteLegal, null=False, on_delete=models.RESTRICT)
    detalle_luminarias = models.ForeignKey(DetalleLuminarias, null=False, on_delete=models.RESTRICT)
    medicion = models.ForeignKey(Medicion, null=False, on_delete=models.RESTRICT)
    estado = models.IntegerField(default=0) 
    creado = models.DateTimeField(default=timezone.now, editable=False)   


    def __str__(self):
        return "{} {} {} {}".format(self.nombre, self.tipo_alumbrado, self.titular.nombre, self.representante_legal.nombre)
    
    class Meta:
        db_table = 'proyecto'
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'