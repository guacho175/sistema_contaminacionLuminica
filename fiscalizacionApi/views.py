import json
from django.shortcuts import render
from django.http import JsonResponse
from fiscalizacion.models import Fiscalizacion, Reporte


# Create your views here.

def cargar_fiscalizaciones(request):
    fiscalizaciones = Fiscalizacion.objects.all()
    data = {
        'fiscalizaciones': list(
            fiscalizaciones.values(
                'id', 'proyecto_id', 'usuario_id', 'creado'
            )
        )
    }
    return JsonResponse(data)


def cargar_reportes(request):
    reportes = Reporte.objects.all()
    data = {
        'reportes': list(
            reportes.values(
                'id', 'fiscalizacion_id', 'creado'
            )
        )
    }
    return JsonResponse(data)


def cargar_fiscalizaciones_completas(request):
    # Obtener datos básicos de fiscalizaciones y reportes
    fiscalizaciones_data = json.loads(cargar_fiscalizaciones(request).content)["fiscalizaciones"]
    reportes_data = {reporte["id"]: reporte for reporte in json.loads(cargar_reportes(request).content)["reportes"]}

    # Construir la respuesta con relaciones anidadas
    for fiscalizacion in fiscalizaciones_data:
        fiscalizacion["reportes"] = [
            reporte for reporte in reportes_data.values() if reporte["fiscalizacion_id"] == fiscalizacion["id"]
        ]


    return JsonResponse({"fiscalizaciones_completas": fiscalizaciones_data})
