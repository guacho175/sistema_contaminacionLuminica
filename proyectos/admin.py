from django.contrib import admin
from .models import Titular, RepresentanteLegal, DetalleLuminarias, Proyecto

# Register your models here.
class TitularAdmin(admin.ModelAdmin):
    list_display = ['id', 'run', 'nombre', 'a_paterno', 'a_materno',
                    'direccon', 'correo']

class RepresentanteLegalAdmin(admin.ModelAdmin):
    list_display = ['id', 'run', 'nombre', 'a_paterno', 'a_materno',
                    'direccon', 'correo']

class DetalleLuminariasAdmin(admin.ModelAdmin):
    list_display = ['id', 'cantidad', 'tipo_lampara', 'marca',
                    'modelo', 'potencia', 'fecha_instalacion',
                    'cod_certificacion', 'fecha_certificacion']

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'longitud', 'latitud',
                    'tipo_alumbrado', 'descripcion', 'nv_cumplimiento', 'titular',
                    'representante_legal', 'detalle_luminarias']

admin.site.register(Titular, TitularAdmin)
admin.site.register(RepresentanteLegal, RepresentanteLegalAdmin)
admin.site.register(DetalleLuminarias, DetalleLuminariasAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
