from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MedicionForm
from services.mediciones.medicionCRUD import MedicionCRUD
from fiscalizacion.models import Fiscalizacion
from .models import Medicion

@login_required
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

@login_required
def eliminar_medicion(request, medicion_id):
    """Vista para eliminar una medición."""
    service = MedicionCRUD(request)
    medicion = service.eliminar_medicion(medicion_id)

    if request.method == 'POST' and medicion.fiscalizacion:
        Fiscalizacion_id = medicion.fiscalizacion.id
        return redirect(f'/fiscalizacion/{Fiscalizacion_id}/detalle/')

    return render(request, 'mediciones/medicionDel.html', {'medicion': medicion})

@login_required
def cargar_editar_medicion(request, medicion_id):
    medicion = get_object_or_404(Medicion, id=medicion_id)
    form = MedicionForm(instance=medicion)
    
    return render(request, 'mediciones/medicionEdit.html', {'form':form, 'medicion':medicion})

@login_required
def editar_medicion(request, medicion_id):
    medicion = get_object_or_404(Medicion, id=medicion_id)
    Fiscalizacion_id = medicion.fiscalizacion.id


    if request.method == 'POST':
        form = MedicionForm(request.POST, request.FILES, instance=medicion)
        if form.is_valid():
            if 'foto' in request.FILES:
                medicion.foto = request.FILES['foto'] # Asignamos imagen

            form.save()
            messages.success(request, 'La medición se modifico correctamente.')

            return redirect(f'/fiscalizacion/{Fiscalizacion_id}/detalle/')
        
        else:
            if 'foto' in form.errors:
                messages.warning(request, form.errors['foto'][0])  # Muestra el primer error relacionado con 'foto'
                return redirect(f'/medicionEdit/{medicion_id}')

    else:
        form = MedicionForm(instance=medicion)
    
    return render(request, 'fiscalizacion/mantenedor_fisclaizacion.html', {'form':form})