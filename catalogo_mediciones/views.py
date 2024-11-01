from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto
from .forms import ProyectoForm
import folium
from folium.plugins import MarkerCluster


def catalogo_mediciones(request):


    context = {

    }

    return render(request, 'catalogo_mediciones/catalogo_mediciones.html', context)


def registrar_medicion(request):
    

    return render(request, 'catalogo_mediciones/registrar_medicion.html')


def detalle_medicion(request, id):
    # Obtener la medición del catálogo


    context = {

    }
    return render(request, 'catalogo_mediciones/detalle_medicion.html', context)


def eliminar_medicion(request, id):
    # Obtener la medición del catálogo

    # Redirigir de vuelta al catálogo
    return redirect('catalogo')


def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../../catalogo/proyectos')
    else:
        form = ProyectoForm()

    # retornamos el formulario
    return render(request, 'catalogo_mediciones/proyectoAdd.html', {'form':form})


def mantenedor_proyecto(request):
    proyectos = Proyecto.objects.all()
    data = {
        'proyectos': proyectos
    }
    return render(request, 'catalogo_mediciones/mantenedor_proyectos.html', data)