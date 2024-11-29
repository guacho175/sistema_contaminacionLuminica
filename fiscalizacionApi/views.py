import json
from django.shortcuts import render
from django.http import JsonResponse
from fiscalizacion.models import Fiscalizacion, Reporte
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt


User = get_user_model()  # Obtén el modelo de usuario activo
@csrf_exempt

def api_login(request):
    print(f"Método recibido: {request.method}")
    print(f"Headers: {request.headers}")
    print(f"Cuerpo: {request.body}")
    if request.method == "POST":
        try:
            # Decodificar el cuerpo JSON de la solicitud
            body = json.loads(request.body)
            username = body.get("username")
            password = body.get("password")

            # Validar que los campos obligatorios estén presentes
            if not username or not password:
                return JsonResponse({"error": "Faltan campos username o password"}, status=400)

            # Autenticar al usuario
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                data = {
                    "id": usuario.id,
                    "username": usuario.username,
                    "email": usuario.email  # Verifica que el campo 'email' exista en tu modelo
                }
                return JsonResponse(data, status=200)
            else:
                return JsonResponse({"error": "Usuario o contraseña incorrectos"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

    # Respuesta para métodos no permitidos
    print(f"Método no permitido: {request.method}")
    return JsonResponse({"error": "Método no permitido"}, status=405)




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
