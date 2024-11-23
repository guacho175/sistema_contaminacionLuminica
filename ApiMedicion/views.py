from django.shortcuts import render
from mediciones.models import InstrumentoMedicion,Medicion
from usuarios.models import Cargo, Institucion, Usuario
from proyectos.models import Proyecto
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def ApiInstrumentoMedicion(request):
    instrumentos = InstrumentoMedicion.objects.all()
    data = {
        'instrumentosMedicion':list(
            instrumentos.values('id', 'tipo', 'marca', 'modelo', 'num_serie')
        )
    }
    return JsonResponse(data)


def ApiProyecto(request):
    proyecto = Proyecto.objects.all()
    data = { 
        'proyectos':list(
            proyecto.values('id','nombre','latitud','longitud','tipo_alumbrado',
                            'descripcion','detalle_luminarias_id','representante_legal_id','titular_id','foto')
        )
    }
    return JsonResponse(data)


@csrf_exempt
def ApiLogin(request):
    if request.method == "POST":
        try:
            #decodificar el cuerpo JSON de la solicitud
            body = json.loads(request.body)
            correo = body.get("correo")
            clave = body.get("clave")

            # Validar que los campos obligatorios estén presentes
            if not correo or not clave:
                return JsonResponse({"error": "Faltan campos correo o clave"}, status=400)

            # obtener el usuario de la base de datos
            try:
                usuario = Usuario.objects.get(correo=correo, clave=clave)
                data = {
                    "id": usuario.id,
                    "correo": usuario.correo
                }
                return JsonResponse(data, status=200)
            except Usuario.DoesNotExist:
                return JsonResponse({"error": "Usuario no encontrado"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

    # Respuesta para métodos no permitidos
    return JsonResponse({"error": "Método no permitido"}, status=405)


