import json
from django.http import JsonResponse
from django.shortcuts import render
from usuarios.models import Usuario,Cargo,Persona,Institucion
# Create your views here.


def cargar_cargos(request):
    cargos = Cargo.objects.all()
    data = {
        'cargos':list(
            cargos.values('id','nombre','descripcion')
        )
    }
    return JsonResponse(data)

def cargar_instituciones(request):
    instituciones = Institucion.objects.all()
    data = {
        'instituciones':list(
            instituciones.values('id','nombre','descripcion')
        )
    }
    return JsonResponse(data)

def cargar_personas(request):
    personas = Persona.objects.all()
    data = {
        'personas':list(
            personas.values('id','nombre','a_paterno','a_materno','correo')
        )
    }
    return JsonResponse(data)

def cargar_usuarios(request):
    usuarios = Usuario.objects.all()
    data = {
        'usuarios':list(
            usuarios.values('id','cargo','institucion')
        )
    }
    return JsonResponse(data)


def cargar_usuarios_completos(request):
    # Convertir las respuestas en diccionarios
    cargos_data = {cargo["id"]: cargo for cargo in json.loads(cargar_cargos(request).content)["cargos"]}
    instituciones_data = {institucion["id"]: institucion for institucion in json.loads(cargar_instituciones(request).content)["instituciones"]}
    personas_data = {persona["id"]: persona for persona in json.loads(cargar_personas(request).content)["personas"]}
    
    usuarios = Usuario.objects.all()
    usuarios_data = []

    for usuario in usuarios:
        usuario_dict = {
            "id": usuario.id,
            "cargo": cargos_data.get(usuario.cargo_id, {}),
            "institucion": instituciones_data.get(usuario.institucion_id, {}),
            "persona": personas_data.get(usuario.id, {})
        }
        usuarios_data.append(usuario_dict)

    return JsonResponse({"usuarios_completos": usuarios_data})
