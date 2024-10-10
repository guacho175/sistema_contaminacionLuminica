from django.shortcuts import render
import folium

# Create your views here.
def mapa(request):
    initialMap = folium.Map(location=[-29.9055324,-71.2313308], zoom_start=10)
    context = {'map':initialMap._repr_html_()}
    return render(request, 'mapa/mapa_mediciones.html', context)