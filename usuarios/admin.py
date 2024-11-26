from django.contrib import admin
from .models import Cargo, Institucion, Usuario

# Register your models here.
class CargoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion']

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'run', 'nombre', 'a_paterno',
                    'a_materno', 'correo', 'cargo',
                    'institucion']


admin.site.register(Cargo, CargoAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Usuario, UsuarioAdmin)