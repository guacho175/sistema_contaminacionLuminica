from django.shortcuts import render
from .models import Usuario

from django.contrib.auth.models import User

def mostrar_usuarios(request):
    usuarios = User.objects.all()
    
    return render(request, 'usuarios/mantenedor_usuarios.html', {'usuarios': usuarios})

# Create your views here.
def cargar_usuario(request):
    usuarios = Usuario.objects.all()
    
    data = {
        'usuarios': usuarios
    }
    return render(request, 'usuarios/mantenedor_usuarios.html', data)