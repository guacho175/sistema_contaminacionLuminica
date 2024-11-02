from django.shortcuts import render, get_object_or_404, redirect

from .models import Medicion


def cargar_medicion(request):
    mediciones = Medicion.objects.all()
    
    data = {
        'mediciones': mediciones
    }
    return render(request, 'catalogo_mediciones/mantenedor_catalogoMedicion.html', data)




