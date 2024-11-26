from django.contrib import admin
from .models import InstrumentoMedicion, Medicion

# Register your models here.
class InstrumentoMedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'marca', 'modelo', 'num_serie']


class MedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'fiscalizacion', 'latitud', 'longitud',  'temperatura', 'humedad', 'valor_medido', 'cumplimiento', 'observacion', 'instrumento_medicion', 'creado']

admin.site.register(InstrumentoMedicion, InstrumentoMedicionAdmin)
admin.site.register(Medicion, MedicionAdmin)

