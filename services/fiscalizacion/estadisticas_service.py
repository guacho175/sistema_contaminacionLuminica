from django.db.models import Min, Max, Avg


class EstadisticasService:
    """Servicio para calcular estadísticas de mediciones."""
    
    
    @staticmethod
    def calcular_estadisticas(mediciones):
        estadisticas = mediciones.aggregate(
            valor_minimo=Min('valor_medido'),
            valor_maximo=Max('valor_medido'),
            valor_promedio=Avg('valor_medido'),
        )
        
        # Redondear los valores y manejar nulos
        return {
            'valor_minimo': round(estadisticas['valor_minimo'], 2) if estadisticas['valor_minimo'] is not None else None,
            'valor_maximo': round(estadisticas['valor_maximo'], 2) if estadisticas['valor_maximo'] is not None else None,
            'valor_promedio': round(estadisticas['valor_promedio'], 2) if estadisticas['valor_promedio'] is not None else None,
        }
    
 
    @staticmethod
    def calcular_porcentaje_cumplimiento(mediciones):
        """
        Calcula el porcentaje de mediciones que cumplen (cumplimiento = '1').
        """
        total_mediciones = mediciones.count()
        mediciones_cumplen = mediciones.filter(cumplimiento='1').count()
        mediciones_no_cumplen = mediciones.filter(cumplimiento='0').count()
        mediciones_evaluadas = mediciones_cumplen + mediciones_no_cumplen

        # Evitar división por cero y manejar escenarios sin mediciones
        if mediciones_evaluadas == 0:
            return None

        porcentaje = (mediciones_cumplen / total_mediciones) * 100

        return round(porcentaje, 2)