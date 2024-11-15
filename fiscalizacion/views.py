from django.shortcuts import render, get_object_or_404, redirect

from .models import Fiscalizacion

from mediciones.models import Medicion
from .forms import FiscalizacionForm

import folium
from folium.plugins import MarkerCluster


# Create your views here.
def inicio(request):
    return render(request, 'proyectos/mantenedor_proyectos.html')




def crear_mapa():
    # Crear el mapa con configuración inicial 
    initialMap = folium.Map(
        location=[-30.031066, -71.280182],
        zoom_start=11,
        #scrollWheelZoom=False  # Desactiva el zoom con la rueda de desplazamiento
        )
    
    return initialMap # Pasar el mapa como HTML


""" # Función para agregar áreas rectangulares basadas en proyectos
def agregar_areas_rectangulares(mapa):
    
    proyectos = Proyecto.objects.all()

    for proyecto in proyectos:
        lat = proyecto.latitud
        lng = proyecto.longitud
        # Ajusta las coordenadas para definir los límites del rectángulo
        bounds = [[lat - 0.0003, lng - 0.0003], [lat + 0.0003, lng + 0.0003]]
        
        kw = {
        "color": "blue",
        "line_cap": "round",
        "fill": True,
        "fill_color": "red",
        "weight": 5,
        #"popup": "Tokyo, Japan",
        "tooltip": f'Área del Proyecto {proyecto.nombre}',
        }
        folium.Rectangle(bounds=bounds, **kw).add_to(mapa)


def agregar_marcadores_mediciones(mapa, mediciones):
    marker_cluster = MarkerCluster().add_to(mapa)
    for medicion in mediciones:
        lat = medicion.latitud
        lng = medicion.longitud
        tooltip = f'Medición en {lat}, {lng}'
        folium.Marker(
            location=[lat, lng],
            popup=f'Valor medido: {medicion.valor_medido}',
            tooltip=tooltip
        ).add_to(marker_cluster) """


# Vista para cargar mediciones y el mapa con áreas
def cargar_fiscalizacion(request):
    fiscalizaciones = Fiscalizacion.objects.all()
    form = FiscalizacionForm()

    # Crear el mapa
    mapa = crear_mapa()

    # Agregar las areas
    #agregar_areas_rectangulares(mapa)

    # Agregar marcadores de mediciones
    #agregar_marcadores_mediciones(mapa, fiscalizaciones)
    
    # Convertir el mapa a HTML para el contexto después de agregar todas las áreas
    map_html = mapa._repr_html_()
    data = {
        'fiscalizaciones': fiscalizaciones,
        'form': form,
        'map': map_html
    }
    return render(request, 'fiscalizacion/mantenedor_fiscalizacion.html', data)


