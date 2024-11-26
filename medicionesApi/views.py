import json
from django.shortcuts import render
from django.http import JsonResponse
from mediciones.models import InstrumentoMedicion, Medicion


# Create your views here.

def cargar_instrumentos_medicion(request):
    instrumentos = InstrumentoMedicion.objects.all()
    data = {
        'instrumentos': list(
            instrumentos.values(
                'id', 'tipo', 'marca', 'modelo', 'num_serie'
            )
        )
    }
    return JsonResponse(data)


def cargar_mediciones(request):
    mediciones = Medicion.objects.all()
    data = {
        'mediciones': list(
            mediciones.values(
                'id', 'tipo', 'latitud', 'longitud', 'temperatura', 'humedad',
                'valor_medido', 'cumplimiento', 'observacion', 'foto', 
                'instrumento_medicion_id', 'fiscalizacion_id', 'creado'
            )
        )
    }
    return JsonResponse(data)

#Vista que carga la Api
def cargar_mediciones_completas(request):
    # Obtener datos básicos de instrumentos y mediciones
    instrumentos_data = {instrumento["id"]: instrumento for instrumento in json.loads(cargar_instrumentos_medicion(request).content)["instrumentos"]}
    mediciones_data = json.loads(cargar_mediciones(request).content)["mediciones"]

    # Construir la respuesta con relaciones anidadas
    for medicion in mediciones_data:
        medicion["instrumento_medicion"] = instrumentos_data.get(medicion["instrumento_medicion_id"], {})
        # Eliminar los IDs relacionados para evitar redundancia en la API
        del medicion["instrumento_medicion_id"]
        del medicion["fiscalizacion_id"]

    return JsonResponse({"mediciones_completas": mediciones_data})
