import datetime
import json
from django.shortcuts import render
from django.http import JsonResponse
from fiscalizacion.models import Fiscalizacion
from mediciones.models import InstrumentoMedicion, Medicion, Sensor
from django.views.decorators.csrf import csrf_exempt



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


    return JsonResponse({"mediciones_completas": mediciones_data})


@csrf_exempt
def guardar_medicion(request):
    if request.method == "POST":
        try:
            # Obtener datos de la solicitud
            instrumento_medicion_id = request.POST.get("instrumento_medicion_id")
            fiscalizacion_id = request.POST.get("fiscalizacion_id")
            tipo = request.POST.get("tipo")
            latitud = request.POST.get("latitud")
            longitud = request.POST.get("longitud")
            temperatura = request.POST.get("temperatura")
            humedad = request.POST.get("humedad")
            valor_medido = request.POST.get("valor_medido")
            cumplimiento = request.POST.get("cumplimiento")
            observacion = request.POST.get("observacion")
            foto = request.FILES.get("foto")

            # Validar campos requeridos
            if not (instrumento_medicion_id and fiscalizacion_id and latitud and longitud and valor_medido):
                return JsonResponse({"error": "Faltan campos requeridos"}, status=400)

            # Verificar relaciones de claves foráneas
            try:
                instrumento_medicion = InstrumentoMedicion.objects.get(id=instrumento_medicion_id)
            except InstrumentoMedicion.DoesNotExist:
                return JsonResponse({"error": "Instrumento de medición no encontrado"}, status=404)

            try:
                fiscalizacion = Fiscalizacion.objects.get(id=fiscalizacion_id)
            except Fiscalizacion.DoesNotExist:
                return JsonResponse({"error": "Fiscalización no encontrada"}, status=404)

            # Crear instancia de Medición
            medicion = Medicion(
                tipo=tipo,
                latitud=latitud,
                longitud=longitud,
                temperatura=temperatura,
                humedad=humedad,
                valor_medido=valor_medido,
                cumplimiento=cumplimiento,
                observacion=observacion,
                instrumento_medicion=instrumento_medicion,
                fiscalizacion=fiscalizacion,
            )

            # Guardar foto si se proporciona
            if foto:
                medicion.foto.save(foto.name, foto, save=False)

            # Guardar medición en la base de datos
            medicion.save()

            return JsonResponse({
                "mensaje": "Medición guardada exitosamente",
                "medicion_id": medicion.id,
                "foto_url": medicion.foto.url if foto else None
            }, status=201)

        except Exception as e:
            return JsonResponse({"error": f"Error al guardar la medición: {str(e)}"}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)




@csrf_exempt
def guardar_sensor(request):
    if request.method == 'POST':
        try:
            # Decodificar datos JSON del cuerpo de la solicitud
            data = json.loads(request.body)

            # Extraer el valor enviado
            valor = data.get('valor')

            # Validar que el valor exista
            if valor is None:
                return JsonResponse({'error': 'El campo "valor" es requerido.'}, status=400)

            # Obtener la fecha y hora actuales del sistema
            fecha_actual = datetime.now().date()  # Fecha en formato YYYY-MM-DD
            hora_actual = datetime.now().time()  # Hora en formato HH:MM:SS

            # Crear una nueva entrada en la base de datos
            Sensor.objects.create(valor=valor, fecha=fecha_actual, hora=hora_actual)

            return JsonResponse({'mensaje': 'Dato del sensor guardado con éxito.'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos, no es JSON.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Error interno: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)
