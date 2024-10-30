from django.shortcuts import render, get_object_or_404, redirect
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
