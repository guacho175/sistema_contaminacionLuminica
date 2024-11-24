from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from mediciones.models import InstrumentoMedicion,Medicion
from usuarios.models import Cargo, Institucion, Usuario
from proyectos.models import Proyecto, Titular, RepresentanteLegal, DetalleLuminarias
from fiscalizacion.models import Fiscalizacion, Reporte



#MODELS MEDICION
def cargar_instrumento_medicion(request):
    instrumentos = InstrumentoMedicion.objects.all()
    data = {
        'instrumentosMedicion':list(
            instrumentos.values('id', 'tipo', 'marca', 'modelo', 'num_serie')
        )
    }
    return JsonResponse(data)

def cargar_medicion(request):
    detalle = Medicion.objects.all()
    data ={
        'mediciones':list(
            detalle.values('id','tipo','latitud','longitud','temperatura','humedad','valor_medido','observacion','creado','fiscalizacion_id',
                           'instrumento_medicion_id','foto')
        )
    }
    return JsonResponse(data)


#MODELS USUARIO
@csrf_exempt
def api_login(request):
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

def cargar_cargo(request):
    detalle = Cargo.objects.all()
    data = {
        'cargos':list(
            detalle.values('id','nombre','descripcion')
        )
    }
    return JsonResponse(data)

def cargar_institucion(request):
    detalle = Institucion.objects.all()
    data = {
        'instituciones':list(
            detalle.values('id','nombre','descripcion')
        )
    }
    return JsonResponse(data)

def cargar_usuario(request):
    detalle = Usuario.objects.all()
    data = {
        'usuarios':list(
            detalle.values('id','run','nombre','a_paterno','a_materno','correo','cargo_id','institucion_id',)
        )
    }
    return JsonResponse(data)

# MODELS PROYECTO
def cargar_proyecto(request):
    proyecto = Proyecto.objects.all()
    data = { 
        'proyectos':list(
            proyecto.values('id','nombre','latitud','longitud','tipo_alumbrado',
                            'descripcion','detalle_luminarias_id','representante_legal_id','titular_id','foto')
        )
    }
    return JsonResponse(data)

def cargar_titular(request):
    titular = Titular.objects.all()
    data = {
        'titulares':list(
            titular.values('id','run','nombre','a_paterno','a_materno','direccon','correo')
        )
    }
    return JsonResponse(data)

def cargar_representante_legal(request):
    representante = RepresentanteLegal.objects.all()
    data = {
        'representantes':list(
            representante.values('id','run','nombre','a_paterno','a_materno','direccon','correo')
        )
    }
    return JsonResponse(data)

def cargar_detalle_luminaria(request):
    detalle = DetalleLuminarias.objects.all()
    data = {
        'detalles_luminarias':list(
            detalle.values('id','cantidad','tipo_lampara','marca','modelo',
                           'potencia','fecha_instalacion','cod_certificacion','fecha_certificacion')
        )
    }
    return JsonResponse(data)

def cargar_modelo_proyecto(request):
    proyectos = Proyecto.objects.all().values(
        'id', 'nombre', 'latitud', 'longitud', 'tipo_alumbrado',
        'descripcion', 'detalle_luminarias_id', 'representante_legal_id',
        'titular_id', 'foto'
    )
    titulares = Titular.objects.all().values(
        'id', 'run', 'nombre', 'a_paterno', 'a_materno', 'direccon', 'correo'
    )
    representantes = RepresentanteLegal.objects.all().values(
        'id', 'run', 'nombre', 'a_paterno', 'a_materno', 'direccon', 'correo'
    )
    detalles_luminarias = DetalleLuminarias.objects.all().values(
        'id', 'cantidad', 'tipo_lampara', 'marca', 'modelo',
        'potencia', 'fecha_instalacion', 'cod_certificacion', 'fecha_certificacion'
    )

    data = {
        'proyectos': list(proyectos),
        'titulares': list(titulares),
        'representantes': list(representantes),
        'detalles_luminarias': list(detalles_luminarias)
    }

    return JsonResponse(data)


# MODELS FISCALIZACION
def cargar_fiscalizacion(request):
    detalle = Fiscalizacion.objects.all()
    data = {
        'fiscalizaciones':list(
            detalle.values('id','proyecto_id','usuario_id')
        )
    }
    return JsonResponse(data)


