from django.shortcuts import get_object_or_404, render
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






@csrf_exempt
def guardar_foto_proyecto(request):
    if request.method == "POST":
        try:
            # Obtener datos de la solicitud
            proyecto_id = request.POST.get("proyecto_id")
            foto_contenido = request.FILES.get("foto")

            if not proyecto_id or not foto_contenido:
                return JsonResponse({"error": "Faltan campos requeridos: proyecto_id o foto"}, status=400)

            # Verificar que el proyecto existe
            try:
                proyecto = Proyecto.objects.get(id=proyecto_id)
            except Proyecto.DoesNotExist:
                return JsonResponse({"error": "El proyecto no existe"}, status=404)

            # Guardar la foto automáticamente usando el método definido en el modelo
            proyecto.foto.save(foto_contenido.name, foto_contenido, save=True)

            return JsonResponse({
                "mensaje": "Foto guardada exitosamente",
                "proyecto_id": proyecto.id,
                "foto_url": proyecto.foto.url
            }, status=200)

        except Exception as e:
            return JsonResponse({"error": f"Error al procesar la solicitud: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)




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


def cargar_modelo_usuario(request):
    if request.method == "GET":
        # Obtener datos de Cargo
        cargos = Cargo.objects.all().values('id', 'nombre', 'descripcion')
        
        # Obtener datos de Institucion
        instituciones = Institucion.objects.all().values('id', 'nombre', 'descripcion')
        
        # Obtener datos de Usuario
        usuarios = Usuario.objects.all().values(
            'id', 'run', 'nombre', 'a_paterno', 'a_materno', 'correo', 'cargo_id', 'institucion_id'
        )
        
        # Construir la respuesta JSON
        data = {
            'cargos': list(cargos),
            'instituciones': list(instituciones),
            'usuarios': list(usuarios),
        }
        return JsonResponse(data, status=200)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

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
    proyectos = Proyecto.objects.all()
    data = []

    for proyecto in proyectos:
        detalle_luminarias = get_object_or_404(DetalleLuminarias, id=proyecto.detalle_luminarias_id)
        representante = get_object_or_404(RepresentanteLegal, id=proyecto.representante_legal_id)
        titular = get_object_or_404(Titular, id=proyecto.titular_id)

        # Construir el JSON para cada proyecto
        data.append({
            'id': proyecto.id,
            'nombre': proyecto.nombre,
            'latitud': proyecto.latitud,
            'longitud': proyecto.longitud,
            'tipo_alumbrado': proyecto.tipo_alumbrado,
            'descripcion': proyecto.descripcion,
            'foto': proyecto.foto.url if proyecto.foto else None,  # Convertir ImageField a URL
            'detalle_luminarias': {
                'id': detalle_luminarias.id,
                'cantidad': detalle_luminarias.cantidad,
                'tipo_lampara': detalle_luminarias.tipo_lampara,
                'marca': detalle_luminarias.marca,
                'modelo': detalle_luminarias.modelo,
                'potencia': detalle_luminarias.potencia,
                'fecha_instalacion': detalle_luminarias.fecha_instalacion,
                'cod_certificacion': detalle_luminarias.cod_certificacion,
                'fecha_certificacion': detalle_luminarias.fecha_certificacion,
            },
            'representante_legal': {
                'id': representante.id,
                'nombre': representante.nombre,
                'a_paterno': representante.a_paterno,
                'a_materno': representante.a_materno,
            },
            'titular': {
                'id': titular.id,
                'nombre': titular.nombre,
                'a_paterno': titular.a_paterno,
                'a_materno': titular.a_materno,
            }
        })

    return JsonResponse({'proyectos': data}, safe=False)




# MODELS FISCALIZACION
def cargar_fiscalizacion(request):
    if request.method == "GET":
        # Obtener todas las fiscalizaciones
        detalle = Fiscalizacion.objects.select_related('proyecto', 'usuario').all()

        # Construir el JSON con los nombres en lugar de los IDs
        data = {
            'fiscalizaciones': [
                {
                    'id': fiscalizacion.id,
                    'proyecto_id': fiscalizacion.proyecto.id,
                    'proyecto_nombre': fiscalizacion.proyecto.nombre,  # Nombre del proyecto
                    'usuario_nombre': f"{fiscalizacion.usuario.nombre} {fiscalizacion.usuario.a_paterno}",  # Nombre completo del usuario
                }
                for fiscalizacion in detalle
            ]
        }
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)



