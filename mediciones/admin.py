from django.contrib import admin
from .models import InstrumentoMedicion, Medicion, Sensor

# Register your models here.
class InstrumentoMedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'marca', 'modelo', 'num_serie']


class MedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'fiscalizacion', 'latitud', 'longitud',  'temperatura', 'humedad', 'valor_medido', 'cumplimiento', 'observacion', 'instrumento_medicion', 'creado']


class SensorAdmin(admin.ModelAdmin):
    list_display = ['id','valor','fecha','hora']

admin.site.register(InstrumentoMedicion, InstrumentoMedicionAdmin)
admin.site.register(Medicion, MedicionAdmin)
admin.site.register(Sensor, SensorAdmin)
