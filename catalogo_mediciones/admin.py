from django.contrib import admin
from .models import InstrumentoMedicion, DetalleMedicion, Medicion

# Register your models here.
class InstrumentoMedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'marca', 'modelo', 'num_serie']


class DetalleMedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'longitud', 'latitud', 'temperatura',
                    'humedad', 'valor_medido', 'instrumento_medicion']

class MedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'cumplimiento', 'inspector', 'proyecto',
                    'detalleMedicion']

admin.site.register(InstrumentoMedicion, InstrumentoMedicionAdmin)
admin.site.register(DetalleMedicion, DetalleMedicionAdmin)
admin.site.register(Medicion, MedicionAdmin)

