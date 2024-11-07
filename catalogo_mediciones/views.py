from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicionForm
from .models import Medicion
from proyectos.models import Proyecto
import folium
from folium.plugins import MarkerCluster



def crear_mapa():
    # Crear el mapa con configuración inicial 
    initialMap = folium.Map(
        location=[-30.031066, -71.280182],
        zoom_start=11,
        #scrollWheelZoom=False  # Desactiva el zoom con la rueda de desplazamiento
        )
    
    return initialMap # Pasar el mapa como HTML


# Función para agregar áreas rectangulares basadas en proyectos
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
        ).add_to(marker_cluster)


# Vista para cargar mediciones y el mapa con áreas
def cargar_medicion(request):
    mediciones = Medicion.objects.all()
    form = MedicionForm()

    # Crear el mapa
    mapa = crear_mapa()

    # Agregar las areas
    agregar_areas_rectangulares(mapa)

    # Agregar marcadores de mediciones
    agregar_marcadores_mediciones(mapa, mediciones)
    
    # Convertir el mapa a HTML para el contexto después de agregar todas las áreas
    map_html = mapa._repr_html_()
    data = {
        'mediciones': mediciones,
        'form': form,
        'map': map_html
    }
    return render(request, 'catalogo_mediciones/mantenedor_catalogoMedicion.html', data)


def crear_medicion(request):
    if request.method == 'POST':
        form = MedicionForm(request.POST)
        if form.is_valid():
            nuevo_registro = form.save()
            # Actualizar el estado del proyecto asociado
            proyecto = nuevo_registro.proyecto
            proyecto.estado = 1
            proyecto.save()
            return redirect('/catalogoMedicion/')
    return redirect('/catalogoMedicion/')


def eliminar_medicion(request, medicion_id):
    medicion = get_object_or_404(Medicion, id=medicion_id)
    proyecto = medicion.proyecto

    if request.method == 'POST':
        medicion.delete()
        # Actualizar el estado del proyecto asociado
        proyecto.estado = 0
        proyecto.save()
        return redirect('/catalogoMedicion/')

    return render(request, 'catalogo_mediciones/medicionDel.html', {'medicion': medicion} )

