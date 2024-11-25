from django.shortcuts import get_object_or_404, render, redirect
from services.fiscalizacion.FiscalizacionService import FiscalizacionService
from .forms import FiscalizacionForm
from .models import Fiscalizacion
from django.contrib import messages
from django.db.models import RestrictedError
from services.fiscalizacion.mapa_service import MapaService




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
    fiscalizaciones = Fiscalizacion.objects.all()

    mapa = MapaService.crear_mapa()

    map_html = mapa._repr_html_()

    data = {
        'fiscalizaciones': fiscalizaciones,
        'form': FiscalizacionForm,
        'map' : map_html
    }

    return render(request, 'fiscalizacion/mantenedor_fiscalizacion.html', data)


def eliminar_fiscalizacion(request, fiscalizacion_id):
    """Vista para eliminar una fiscalización."""

    fiscalizacion = get_object_or_404(Fiscalizacion, id=fiscalizacion_id)

    if request.method == 'POST':
        try:
            FiscalizacionService.eliminar_fiscalizacion(fiscalizacion_id)
            messages.success(request, f'El registro {fiscalizacion.proyecto} se eliminó correctamente.')
            return redirect('') 
        except RestrictedError as e:
            messages.error(request, f'No se puede eliminar el registro: {e.args[0]}')

    return render(request, 'fiscalizacion/fiscalizacionDel.html', {'fiscalizacion': fiscalizacion})


def detalle_fiscalizacion(request, fiscalizacion_id):
    fiscalizacion = get_object_or_404(Fiscalizacion, id=fiscalizacion_id)
    
    return render(request, 'fiscalizacion/detalle_fiscalizacion.html', {'fiscalizacion': fiscalizacion})

