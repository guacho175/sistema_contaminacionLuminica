from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import MedicionForm
from services.mediciones.medicionCRUD import MedicionCRUD
from fiscalizacion.models import Fiscalizacion


def nueva_medicion(request, fiscalizacion_id):
    """Vista para ingresar una nueva medición."""
    fiscalizacion = get_object_or_404(Fiscalizacion, id=fiscalizacion_id)

    if request.method == 'POST':
        form = MedicionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medición se ingreso correctamente.')
            return redirect('')
    else:
    # Inicializa el formulario con la fiscalización por defecto
        form = MedicionForm(initial={'fiscalizacion': fiscalizacion})

    # retornamos el formulario
    return render(request, 'mediciones/medicionAdd.html', {'form': form, 'fiscalizacion': fiscalizacion})


def eliminar_medicion(request, medicion_id):
    """Vista para eliminar una medición."""
    service = MedicionCRUD(request)
    medicion = service.eliminar_medicion(medicion_id)

    if request.method == 'POST' and medicion.fiscalizacion:
        proyecto_id = medicion.fiscalizacion.proyecto.id
        return redirect(f'/fiscalizacion/{proyecto_id}/detalle/')

    return render(request, 'mediciones/medicionDel.html', {'medicion': medicion})