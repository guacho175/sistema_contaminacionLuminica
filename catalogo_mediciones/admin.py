from django.contrib import admin
from .models import InstrumentoMedicion, Medicion

# Register your models here.
class InstrumentoMedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'marca', 'modelo', 'num_serie']


class MedicionAdmin(admin.ModelAdmin):
    list_display = ['id', 'cumplimiento', 'inspector', 'latitud', 'longitud', 'temperatura',
                    'humedad', 'valor_medido', 'instrumento_medicion', 'creado']

admin.site.register(InstrumentoMedicion, InstrumentoMedicionAdmin)
admin.site.register(Medicion, MedicionAdmin)

