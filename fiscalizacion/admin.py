from django.contrib import admin
from .models import Fiscalizacion, Reporte

class FiscalizacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'proyecto', 'usuario', 'creado'] 

class ReporteAdmin(admin.ModelAdmin):
    list_display = ['id', 'creado', 'fiscalizacion']

admin.site.register(Fiscalizacion, FiscalizacionAdmin)
admin.site.register(Reporte, ReporteAdmin)
