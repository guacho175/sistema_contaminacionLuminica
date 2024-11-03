from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicionForm
from .models import Medicion
from proyectos.models import Proyecto
import folium


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
 # Obtiene los proyectos asociados a mediciones con estado = 1
    mediciones = Medicion.objects.filter(estado=1)
    proyectos = Proyecto.objects.filter(id__in=mediciones.values('proyecto_id')).distinct()
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

# Vista para cargar mediciones y el mapa con áreas
def cargar_medicion(request):
    mediciones = Medicion.objects.all()
    form = MedicionForm()

    # Crear el mapa y agregar las áreas
    mapa = crear_mapa()
    agregar_areas_rectangulares(mapa)

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

