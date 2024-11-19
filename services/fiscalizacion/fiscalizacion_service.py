from fiscalizacion.models import Fiscalizacion
from mediciones.models import Medicion
from django.db.models import Min, Max, Avg

class FiscalizacionService:
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
            resultado.append({
                'fiscalizacion': fiscalizacion,
                'mediciones': mediciones,
                'estadisticas': estadisticas,
            })
            todas_las_mediciones.extend(mediciones)


        return resultado, todas_las_mediciones
