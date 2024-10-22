from django.shortcuts import render, get_object_or_404, redirect
from .forms import EditarMedicion, MedicionForm
from .models import Tipo_alumbrado_art5, Tipo_alumbrado_art6, CatalogoMedicion


def catalogo_mediciones(request):
    mediciones_catalogo = CatalogoMedicion.objects.all()

    context = {
        'mediciones_catalogo': mediciones_catalogo,
    }

    return render(request, 'catalogo_mediciones/catalogo_mediciones.html', context)


def detalle_medicion(request, id):
    # Obtener la medición del catálogo
    medicion_catalogo = get_object_or_404(CatalogoMedicion, id=id)
    
    # Dependiendo de si es art5 o art6, cargamos el detalle correspondiente
    medicion = None
    tipo_medicion = ""

    if medicion_catalogo.medicion_art5:
        medicion = medicion_catalogo.medicion_art5
        tipo_medicion = "art5"
    elif medicion_catalogo.medicion_art6:
        medicion = medicion_catalogo.medicion_art6
        tipo_medicion = "art6"

    context = {
        'medicion': medicion,
        'tipo_medicion': tipo_medicion
    }
    return render(request, 'catalogo_mediciones/detalle_medicion.html', context)


def editar_medicion(request, id):
    medicion = get_object_or_404(Tipo_alumbrado_art5, id=id)
    
    if request.method == 'POST':
        form = EditarMedicion(request.POST, instance=medicion)
        if form.is_valid():
            form.save()
            return redirect('detalle_medicion', id=id)
    else:
        form = EditarMedicion(instance=medicion)
    
    return render(request, 'catalogo_mediciones/editar_medicion.html', {'form': form})



def registrar_medicion(request):
    if request.method == 'POST':
        form = MedicionForm(request.POST)
        if form.is_valid():
            # Verifica cuál de los dos campos fue seleccionado
            medicion_art5 = form.cleaned_data.get('medicion_art5')
            medicion_art6 = form.cleaned_data.get('medicion_art6')

            # Crear una nueva entrada en CatalogoMedicion
            nueva_medicion_catalogo = CatalogoMedicion()

            if medicion_art5:
                nueva_medicion_catalogo.medicion_art5 = medicion_art5
                medicion_art5.estado = 1  # Cambia el estado de evaluación
                medicion_art5.save()  # Guarda el cambio
            elif medicion_art6:
                nueva_medicion_catalogo.medicion_art6 = medicion_art6
                medicion_art6.estado = 1  # Cambia el estado de evaluación
                medicion_art6.save()  # Guarda el cambio

            nueva_medicion_catalogo.save()  # Guardar en el catálogo

            # Redirigir al catálogo después de guardar
            return redirect('catalogo')
    else:
        form = MedicionForm()

    return render(request, 'catalogo_mediciones/registrar_medicion.html', {'form': form})


def eliminar_medicion(request, id):
    # Obtener la medición del catálogo
    medicion_catalogo = get_object_or_404(CatalogoMedicion, id=id)
    
    # Dependiendo de si es art5 o art6, cambiar el estado de cumplimiento
    if medicion_catalogo.medicion_art5:
        medicion_catalogo.medicion_art5.estado = 0
        medicion_catalogo.medicion_art5.save()
    elif medicion_catalogo.medicion_art6:
        medicion_catalogo.medicion_art6.estado = 0
        medicion_catalogo.medicion_art6.save()
    
    # Eliminar la medición del catálogo
    medicion_catalogo.delete()

    # Redirigir de vuelta al catálogo
    return redirect('catalogo')