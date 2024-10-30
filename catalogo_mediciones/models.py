from django.db import models
from django.utils import timezone
from .choices import tipos_alumbrado, nivel_cumplimiento, tipo_flujo_luminoso

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
        return "{}".format(self.nombre, self.a_paterno, self.a_materno)
    
    class Meta:
        db_table = 'titular'
        verbose_name = 'Titular'
        verbose_name_plural = 'Titulares'