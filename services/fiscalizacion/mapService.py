import folium
from folium.plugins import MarkerCluster
from fiscalizacion.models import Fiscalizacion
from mediciones.models import Medicion
from django.db.models import Min, Max, Avg


class MapService:
    """Servicio para crear mapa."""

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


    @staticmethod
    def obtener_fiscalizaciones_con_mediciones():
        fiscalizaciones = Fiscalizacion.objects.all().select_related('proyecto', 'usuario')
        resultado = []
        todas_las_mediciones = []

        for fiscalizacion in fiscalizaciones:
            mediciones = Medicion.objects.filter(fiscalizacion=fiscalizacion)
            estadisticas = mediciones.aggregate(
                valor_minimo=Min('valor_medido'),
                valor_maximo=Max('valor_medido'),
                valor_promedio=Avg('valor_medido'),
            )
            
            # Redondear los valores
            estadisticas = {
                'valor_minimo': round(estadisticas['valor_minimo'], 2) if estadisticas['valor_minimo'] is not None else None,
                'valor_maximo': round(estadisticas['valor_maximo'], 2) if estadisticas['valor_maximo'] is not None else None,
                'valor_promedio': round(estadisticas['valor_promedio'], 2) if estadisticas['valor_promedio'] is not None else None,
            }
            
            resultado.append({
                'fiscalizacion': fiscalizacion,
                'mediciones': mediciones,
                'estadisticas': estadisticas,
            })
            todas_las_mediciones.extend(mediciones)


        return resultado, todas_las_mediciones




 


