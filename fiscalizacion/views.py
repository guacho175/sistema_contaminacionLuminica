from django.shortcuts import get_object_or_404, render, redirect
from .forms import FiscalizacionForm
from .models import Fiscalizacion
from django.contrib import messages
from django.db.models import RestrictedError
from proyectos.models import Proyecto

from services.fiscalizacion.fiscalizacion_service import FiscalizacionService
from services.fiscalizacion.map_service import MapService
from services.fiscalizacion.estadisticas_service import EstadisticasService




def crear_fiscalizacion(request) -> None:
    """Vista para crear una nueva fiscalización."""

    if request.method == 'POST':
        form = FiscalizacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fiscalización ingresada exitosamente al sistema.')
            return redirect('')  
        else:
            messages.error(request, 'Hubo un error al crear la fiscalización. Revisa los datos ingresados.')


def cargar_fiscalizaciones(request) -> dict:
    """Carga las fiscalizaciones con sus mediciones y genera el mapa."""

    # Obtener datos de la capa services
    fiscalizaciones_con_mediciones, todas_las_mediciones = FiscalizacionService.obtener_fiscalizaciones_con_mediciones()
   
    
    # Crear el mapa
    mapa = MapService.crear_mapa()
    MapService.agregar_areas_rectangulares(mapa, Proyecto.objects.all())
    MapService.agregar_marcadores_mediciones(mapa, todas_las_mediciones)

    # Renderizar el mapa
    map_html = mapa._repr_html_()

    # Preparar el contexto
    data = {
        'form': FiscalizacionForm,
        'map' : map_html,
        'fiscalizaciones_con_mediciones': fiscalizaciones_con_mediciones,
    }

    return render(request, 'fiscalizacion/mantenedor_fiscalizacion.html', data)


def eliminar_fiscalizacion(request, fiscalizacion_id):
    """Vista para eliminar una fiscalización."""

    fiscalizacion = get_object_or_404(Fiscalizacion, id=fiscalizacion_id)

    if request.method == 'POST':
        try:
            fiscalizacion.delete()
            messages.success(request, f'El registro {fiscalizacion.proyecto} se eliminó correctamente.')
            return redirect('') 
        except RestrictedError as e:
            messages.error(request, f'No se puede eliminar el registro: {e.args[0]}')

    return render(request, 'fiscalizacion/fiscalizacionDel.html', {'fiscalizacion': fiscalizacion})


def detalle_fiscalizacion(request, fiscalizacion_id):
    # Obtener la fiscalización y sus mediciones
    fiscalizacion = get_object_or_404(Fiscalizacion, id=fiscalizacion_id)
    mediciones = fiscalizacion.medicion_set.all()

    # Calcular el porcentaje de cumplimiento utilizando el servicio
    porcentaje_cumplimiento = EstadisticasService.calcular_porcentaje_cumplimiento(mediciones)
    
    
    return render(request, 'fiscalizacion/detalle_fiscalizacion.html', {'fiscalizacion': fiscalizacion, 'porcentaje_cumplimiento': porcentaje_cumplimiento})

