from django.contrib import admin
from .models import Titular, RepresentanteLegal, DetalleLuminaria, Proyecto

# Register your models here.
class TitularAdmin(admin.ModelAdmin):
    list_display = ['id', 'run', 'nombre', 'a_paterno', 'a_materno',
                    'direccion', 'correo']

class RepresentanteLegalAdmin(admin.ModelAdmin):
    list_display = ['id', 'run', 'nombre', 'a_paterno', 'a_materno',
                    'direccion', 'correo']

class DetalleLuminariasAdmin(admin.ModelAdmin):
    list_display = ['id', 'cantidad', 'tipo_lampara', 'marca',
                    'modelo', 'potencia', 'fecha_instalacion',
                    'cod_certificacion', 'fecha_certificacion']

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'longitud', 'latitud',
                    'tipo_alumbrado', 'descripcion', 'titular',
                    'representante_legal', 'detalle_luminarias','foto']

admin.site.register(Titular, TitularAdmin)
admin.site.register(RepresentanteLegal, RepresentanteLegalAdmin)
admin.site.register(DetalleLuminaria, DetalleLuminariasAdmin)
admin.site.register(Proyecto, ProyectoAdmin)

