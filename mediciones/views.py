from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MedicionForm
from services.mediciones.medicionCRUD import MedicionCRUD


def nueva_medicion(request, fiscalizacion_id):
    """Vista para ingresar una nueva medición."""
    if request.method == 'POST':
        form = MedicionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'El proyecto se ingreso correctamente.')
            return redirect('/proyectos/')
    else:
        form = MedicionForm()

    # retornamos el formulario
    return render(request, 'mediciones/medicionAdd.html', {'form': form})




    service = MedicionCRUD(request)

    if request.method == "POST":
        form = MedicionForm(request.POST, request.FILES)
        response = service.crear_medicion(fiscalizacion_id, form)
        if response:
            return response

    else:
        form = MedicionForm()

    return render(request, 'mediciones/medicionAdd.html', {'form': form})


def eliminar_medicion(request, medicion_id):
    """Vista para eliminar una medición."""
    service = MedicionCRUD(request)
    medicion = service.eliminar_medicion(medicion_id)

    if request.method == 'POST' and medicion.fiscalizacion:
        proyecto_id = medicion.fiscalizacion.proyecto.id
        return redirect(f'/fiscalizacion/{proyecto_id}/detalle/')

    return render(request, 'mediciones/medicionDel.html', {'medicion': medicion})