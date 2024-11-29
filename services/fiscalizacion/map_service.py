import folium
from folium.plugins import MarkerCluster

class MapService:
    """Servicio para crear y gestionar mapas."""
    
    @staticmethod
    def crear_mapa():
        return folium.Map(location=[-30.031066, -71.280182], zoom_start=11)
    
    @staticmethod
    def agregar_areas_rectangulares(mapa, proyectos):
        for proyecto in proyectos:
            lat, lng = proyecto.latitud, proyecto.longitud
            bounds = [[lat - 0.0003, lng - 0.0003], [lat + 0.0003, lng + 0.0003]]
            folium.Rectangle(
                bounds=bounds, color="blue", line_cap="round", fill=True,
                fill_color="red", weight=5, tooltip=f'Área del Proyecto {proyecto.nombre}'
            ).add_to(mapa)
    
    @staticmethod
    def agregar_marcadores_mediciones(mapa, mediciones):
        marker_cluster = MarkerCluster().add_to(mapa)
        for medicion in mediciones:
            lat, lng = medicion.latitud, medicion.longitud
            folium.Marker(
                location=[lat, lng],
                popup=f'Valor medido: {medicion.valor_medido}',
                tooltip=f'Medición en {lat}, {lng}'
            ).add_to(marker_cluster)
