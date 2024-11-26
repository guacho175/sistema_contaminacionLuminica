import json
from django.shortcuts import render
from django.http import JsonResponse
from proyectos.models import Proyecto,RepresentanteLegal,Titular,DetalleLuminaria


# Create your views here.

def cargar_proyecto(request):
    proyecto = Proyecto.objects.all()
    data = { 
        'proyectos':list(
            proyecto.values('id','nombre','latitud','longitud','tipo_alumbrado',
                            'descripcion','detalle_luminarias_id','representante_legal_id','titular_id')
        )
    }
    return JsonResponse(data)

def cargar_titular(request):
    titular = Titular.objects.all()
    data = {
        'titulares':list(
            titular.values('id','run','nombre','a_paterno','a_materno','direccion','correo')
        )
    }
    return JsonResponse(data)

def cargar_representante_legal(request):
    representante = RepresentanteLegal.objects.all()
    data = {
        'representantes':list(
            representante.values('id','run','nombre','a_paterno','a_materno','direccion','correo')
        )
    }
    return JsonResponse(data)

def cargar_detalle_luminaria(request):
    detalle = DetalleLuminaria.objects.all()
    data = {
        'detalles_luminarias':list(
            detalle.values('id','cantidad','tipo_lampara','marca','modelo',
                           'potencia','fecha_instalacion','cod_certificacion','fecha_certificacion')
        )
    }
    return JsonResponse(data)



def cargar_proyectos_completos(request):
    # Uso funciones creadas previamente
    # Convertir las respuestas en diccionarios

    proyectos_data = json.loads(cargar_proyecto(request).content)["proyectos"]
    titulares_data = {titular["id"]: titular for titular in json.loads(cargar_titular(request).content)["titulares"]}
    representantes_data = {representante["id"]: representante for representante in json.loads(cargar_representante_legal(request).content)["representantes"]}
    detalles_luminarias_data = {detalle["id"]: detalle for detalle in json.loads(cargar_detalle_luminaria(request).content)["detalles_luminarias"]}

    # Construir la respuesta con relaciones anidadas
    for proyecto in proyectos_data:
        proyecto["titular"] = titulares_data.get(proyecto["titular_id"], {})
        proyecto["representante_legal"] = representantes_data.get(proyecto["representante_legal_id"], {})
        proyecto["detalle_luminarias"] = detalles_luminarias_data.get(proyecto["detalle_luminarias_id"], {})
        # Eliminar los IDs relacionados para evitar redundancia en la API
        del proyecto["titular_id"]
        del proyecto["representante_legal_id"]
        del proyecto["detalle_luminarias_id"]

    return JsonResponse({"proyectos": proyectos_data})
