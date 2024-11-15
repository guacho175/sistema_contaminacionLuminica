from django.shortcuts import render
from .models import Usuario

# Create your views here.
def cargar_usuario(request):
    usuarios = Usuario.objects.all()
    
    data = {
        'usuarios': usuarios
    }
    return render(request, 'usuarios/mantenedor_usuarios.html', data)