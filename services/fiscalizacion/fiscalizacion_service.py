from fiscalizacion.models import Fiscalizacion
from mediciones.models import Medicion
from services.fiscalizacion.estadisticas_service import EstadisticasService


class FiscalizacionService:
    """Servicio para gestionar fiscalizaciones."""
    

    @staticmethod
    def obtener_fiscalizaciones_con_mediciones():
        fiscalizaciones = Fiscalizacion.objects.all().select_related('proyecto', 'usuario')
        resultado = []
        todas_las_mediciones = []

        for fiscalizacion in fiscalizaciones:
            mediciones = Medicion.objects.filter(fiscalizacion=fiscalizacion)
            estadisticas = EstadisticasService.calcular_estadisticas(mediciones)
            porcentaje_cumplimiento = EstadisticasService.calcular_porcentaje_cumplimiento(mediciones)

            
            resultado.append({
                'fiscalizacion': fiscalizacion,
                'mediciones': mediciones,
                'estadisticas': estadisticas,
                'porcentaje_cumplimiento': porcentaje_cumplimiento,

            })
            todas_las_mediciones.extend(mediciones)

        return resultado, todas_las_mediciones
