from django.shortcuts import render, get_object_or_404, redirect
from .models import Fiscalizacion
from proyectos.models import Proyecto
from mediciones.models import Medicion
from django.db.models import Min, Max, Avg
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
def cargar_fiscalizacion(request):
    fiscalizaciones = Fiscalizacion.objects.all().select_related('proyecto', 'usuario')

    # Crear un diccionario para mapear mediciones a sus fiscalizaciones junto con estadísticas
    fiscalizaciones_con_mediciones = []
    
    todas_las_mediciones = []  # Lista para almacenar todas las mediciones

    for fiscalizacion in fiscalizaciones:
        mediciones = Medicion.objects.filter(fiscalizacion=fiscalizacion)

        # Calcular estadísticas de las mediciones
        estadisticas = mediciones.aggregate(
            valor_minimo=Min('valor_medido'),
            valor_maximo=Max('valor_medido'),
            valor_promedio=Avg('valor_medido'),
        )

        fiscalizaciones_con_mediciones.append({
            'fiscalizacion': fiscalizacion,
            'mediciones': mediciones,
            'estadisticas': estadisticas
        })

        todas_las_mediciones.extend(mediciones)  # Agregar mediciones a la lista

    # Crear el mapa
    mapa = crear_mapa()

    # Agregar las áreas
    agregar_areas_rectangulares(mapa)

    # Agregar marcadores de mediciones
    agregar_marcadores_mediciones(mapa, todas_las_mediciones)
    
    # Convertir el mapa a HTML para el contexto después de agregar todas las áreas
    map_html = mapa._repr_html_()
    data = {
        'fiscalizaciones_con_mediciones': fiscalizaciones_con_mediciones,
        'map': map_html
    }
    return render(request, 'fiscalizacion/mantenedor_fiscalizacion.html', data)


def detalle_fiscalizacion(request, proyecto_id):
    # Obtener el proyecto con el ID proporcionado
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    
    # Obtener las mediciones asociadas a las fiscalizaciones del proyecto
    mediciones = Medicion.objects.filter(fiscalizacion__proyecto=proyecto).select_related('fiscalizacion__usuario')
    
    data = {
        'proyecto': proyecto,
        'mediciones': mediciones
    }
    return render(request, 'fiscalizacion/detalle_fiscalizacion.html', data)
