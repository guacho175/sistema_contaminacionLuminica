from django.db import models
from django.utils import timezone

class Cargo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')

    def __str__(self):
        return "{} {}".format(self.nombre, self.descripcion)
        
    class Meta:
        db_table = 'cargo'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'


class Institucion(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')

    def __str__(self):
        return "{} {}".format(self.nombre, self.descripcion)

    class Meta:
        db_table = 'institucion'
        verbose_name = 'Institucion'
        verbose_name_plural = 'Instituciones'

class Usuario(models.Model):
    run = models.CharField(max_length=15, verbose_name='Run')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    a_paterno = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    a_materno = models.CharField(max_length=50, verbose_name='Apellido Materno')
    correo = models.CharField(max_length=100, verbose_name='Correo')
    cargo = models.ForeignKey(Cargo, null=False, on_delete=models.RESTRICT)
    institucion = models.ForeignKey(Institucion, null=False, on_delete=models.RESTRICT)
    creado = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "{} {} {} {}".format(self.run ,self.nombre, self.a_paterno, self.a_materno)
        
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'