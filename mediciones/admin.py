from django.contrib import admin
from .models import InstrumentoMedicion, Medicion, Sensor, MedicionSensor

# Register your models here.
class MedicionSensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperatura', 'humedad', 'luminancia', 'iluminancia']

class SensorAdmin(admin.ModelAdmin):
    list_display = ['id','latitud','longitud']

class InstrumentoMedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'marca', 'modelo', 'num_serie']


class MedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'fiscalizacion', 'latitud', 'longitud',  'temperatura', 'humedad', 'valor_medido', 'cumplimiento', 'observacion', 'instrumento_medicion', 'creado']

admin.site.register(InstrumentoMedicion, InstrumentoMedicionAdmin)
admin.site.register(Medicion, MedicionAdmin)
admin.site.register(MedicionSensor, MedicionSensorAdmin)
admin.site.register(Sensor, SensorAdmin)


