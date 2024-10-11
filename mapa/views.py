from django.shortcuts import render
from .models import Location 
import folium

# Create your views here.
def mapa(request):
    initialMap = folium.Map(location=[-29.9055324, -71.2313308], zoom_start=10)
    
    # Itera sobre las ubicaciones guardadas en la base de datos y añade un marcador por cada una
    sensors = Location.objects.all()  # Obtiene todos los sensores
    for sensor in sensors:
        # Determina el icono basado en el valor de cumplimiento
        if sensor.cumpl == 0:
            icon = folium.Icon(icon="minus-sign", prefix="glyphicon", color="gray")
        elif sensor.cumpl == 1:
            icon = folium.Icon(icon="remove-sign", prefix="glyphicon", color="red")
        else:
            icon = folium.Icon(icon="ok-sign", prefix="glyphicon", color="green")
        
        folium.Marker(
            location=[sensor.lat, sensor.lng],
            popup=sensor.name,  # Muestra el nombre del sensor al hacer clic
            tooltip=sensor.address,  # Muestra la dirección cuando se pasa el cursor
            icon=icon  # Usa el icono definido anteriormente 
        ).add_to(initialMap)

    # Renderiza el mapa con los marcadores en el template
    context = {'map':initialMap._repr_html_()}
    return render(request, 'mapa/mapa_mediciones.html', context)