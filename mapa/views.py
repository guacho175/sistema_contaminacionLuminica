from django.shortcuts import render
from .models import Location 
import folium
from folium.plugins import MarkerCluster

def mapa(request):
    # Recupero todas los sensores
    locations = Location.objects.all()

    # Defino el mapa
    initialMap = folium.Map(location=[-29.9055324, -71.2313308], zoom_start=10)

    # Creamos el objeto de Clustering para agrupar los marcadores
    marker_cluster = MarkerCluster().add_to(initialMap)

    # Itera sobre las ubicaciones y añade cada marcador con su icono al cluster
    for sensor in locations:
        # Determina el icono basado en el valor de cumplimiento
        if sensor.cumpl == 0:
            icon = folium.Icon(icon="minus-sign", prefix="glyphicon", color="gray")
        elif sensor.cumpl == 1:
            icon = folium.Icon(icon="remove-sign", prefix="glyphicon", color="red")
        else:
            icon = folium.Icon(icon="ok-sign", prefix="glyphicon", color="green")

        # Añade el marcador al cluster
        folium.Marker(
            location=[sensor.lat, sensor.lng],
            popup=sensor.name,  # Muestra el nombre del sensor al hacer clic
            tooltip=sensor.address,  # Muestra la dirección cuando se pasa el cursor
            icon=icon  # Usa el icono definido anteriormente 
        ).add_to(marker_cluster)

    # Renderiza el mapa con los marcadores en el template
    context = {'map': initialMap._repr_html_()}
    return render(request, 'mapa/mapa_mediciones.html', context)
