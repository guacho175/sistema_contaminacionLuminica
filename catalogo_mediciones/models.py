from django.db import models
from django.utils import timezone

# Create your models here.


class Rol(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=1000, verbose_name='Descripcion')
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.nombre)
    
    class Meta:
        db_table = 'rol'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'


class Usuario(models.Model):
    run = models.CharField(max_length=10, verbose_name='RUN')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    rol = models.ForeignKey(Rol, null=True, on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {}".format(self.nombre, self.paterno, self.materno)
    
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre', 'paterno', 'materno']


class Tipo_alumbrado_art5(models.Model):
    direccion = models.CharField(max_length=250, verbose_name='Ubicación')
    latitud = models.FloatField(verbose_name='Latitud')
    longitud = models.FloatField(verbose_name='Longitud')
    menor_igual_90grados = models.FloatField(verbose_name='Intensidad Luminosa <= 90º')
    mayor_90grados = models.FloatField(verbose_name='Intensidad Luminosa > 90º')
    clase_luminaria = models.CharField(max_length=50, verbose_name='Clase de luminaria')
    emision_reflexion =  models.FloatField(verbose_name='Emisión por Reflexión')
    proteccion_especial = models.CharField(max_length=2, verbose_name='Área de protección especial')
    radiancia_espectral = models.FloatField(verbose_name='Radiancia Espectral')
    emision_conjunta = models.CharField(max_length=2, verbose_name='Emision conjunta considerada')
    observaciones = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observaciones')
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Medicion_art5'
        verbose_name_plural = 'Mediciones_art5'

    def __str__(self):
        return self.direccion
