from django.shortcuts import render, redirect
from .models import Location
import folium
from folium.plugins import MarkerCluster

def mapa(request):
    # Recupero todas las ubicaciones
    sensors = Location.objects.all()

    # Si es una solicitud POST, actualizo el cumplimiento del sensor seleccionado
    if request.method == 'POST':
        sensor_id = request.POST.get('sensor_id')
        new_cumpl = request.POST.get('cumpl')

        # Actualiza el cumplimiento del sensor seleccionado
        sensor = Location.objects.get(id=sensor_id)
        sensor.cumpl = new_cumpl
        sensor.save()

        # Redirige a la misma vista para actualizar el mapa
        return redirect('mapa')

    # Genero el mapa
    initialMap = folium.Map(location=[-29.9055324, -71.2313308], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(initialMap)

    # Itera sobre los sensores y añade un marcador para cada uno
    for sensor in sensors:
        # Determina el icono basado en el valor de cumplimiento
        if sensor.cumpl == 0:
            icon = folium.Icon(icon="minus-sign", prefix="glyphicon", color="gray")
        elif sensor.cumpl == 1:
            icon = folium.Icon(icon="remove-sign", prefix="glyphicon", color="red")
        elif sensor.cumpl == 2:
            icon = folium.Icon(icon="ok-sign", prefix="glyphicon", color="orange")
        else:
            icon = folium.Icon(icon="ok-sign", prefix="glyphicon", color="green")

        # Añade el marcador al clúster
        folium.Marker(
            location=[sensor.lat, sensor.lng],
            popup=sensor.name,
            tooltip=sensor.address,
            icon=icon
        ).add_to(marker_cluster)

    # Renderiza el mapa y el formulario en el template
    context = {
        'map': initialMap._repr_html_(),
        'sensors': sensors  # Envío los sensores al template para mostrarlos en el formulario
    }
    return render(request, 'mapa/mapa_mediciones.html', context)
