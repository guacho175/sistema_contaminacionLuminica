from django.shortcuts import render, HttpResponse
from .models import areas_protegidas as areas

# Create your views here.
def inicio(request):
    return render(request, 'historialMediciones/inicio.html')

def areas_protegidas(request):
    data = {
        'areas': areas,
    }
    return render(request, 'historialMediciones/areas_protegidas.html', data)
    