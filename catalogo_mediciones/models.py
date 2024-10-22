from django.db import models
from django.utils import timezone
from .choices import tipos_alumbrado, nivel_cumplimiento, tipo_flujo_luminoso

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
    estado = models.IntegerField(default='0')
    tipo_alumbrado = models.CharField(max_length=4,choices=tipos_alumbrado, default='art5')
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


class Tipo_alumbrado_art6(models.Model):
    estado = models.IntegerField(default='0')
    tipo_alumbrado = models.CharField(max_length=4,choices=tipos_alumbrado, default='art6')
    direccion = models.CharField(max_length=250, verbose_name='Ubicación')
    latitud = models.FloatField(verbose_name='Latitud')
    longitud = models.FloatField(verbose_name='Longitud')
    tipo_flujo_luminoso = models.CharField(max_length=1, choices=tipo_flujo_luminoso, default='', verbose_name='Tipo de flujo luminoso')
    valor_flujo_luminoso = models.FloatField(verbose_name='Flujo luminoso de luminaria')
    Hemisferio_superior = models.FloatField(verbose_name='Emision al hemisferio superior')
    proteccion_especial = models.CharField(max_length=2, verbose_name='Área de protección especial')
    reflexion_luminancia = models.FloatField(verbose_name='Emisiòn por Reflexiòn: Luminancia')
    temperatura_luz_blanca = models.FloatField(verbose_name='Temperatura de color: Luz Blanca')
    temperatura_luz_color = models.FloatField(verbose_name='Temperatura de color: Luces multicolor')
    limite_horario = models.CharField(max_length=2, verbose_name='Limite horario')
    horario_extendido = models.CharField(max_length=2, verbose_name='Permiso de extención horaria')
    observaciones = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observaciones')
    usuario = models.ForeignKey(Usuario, null=True, on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Medicion_art6'
        verbose_name_plural = 'Mediciones art6'

    def __str__(self):
        return self.direccion

class CatalogoMedicion(models.Model):
    nivel_cumplimiento = models.CharField(max_length=1, null=True, blank=True, choices=nivel_cumplimiento, default='0')
    medicion_art5 = models.ForeignKey(Tipo_alumbrado_art5, null=True, blank=True, on_delete=models.SET_NULL)
    medicion_art6 = models.ForeignKey(Tipo_alumbrado_art6, null=True, blank=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name = 'Catálogo de Mediciones'
        verbose_name_plural = 'Catálogo de Mediciones'

    def __str__(self):
        if self.medicion_art5:
            return f"Medición Art. 5 - {self.medicion_art5.direccion}"
        elif self.medicion_art6:
            return f"Medición Art. 6 - {self.medicion_art6.direccion}"
        return "Medición sin detalles"
