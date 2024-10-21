from django.shortcuts import render, get_object_or_404, redirect
from .forms import EditarMedicion
from .models import Tipo_alumbrado_art5


def catalogo_mediciones(request):
    mediciones_art5 = Tipo_alumbrado_art5.objects.all()  # Obtenemos todas las mediciones
    context = {
        'mediciones_art5': mediciones_art5
    }
    return render(request, 'catalogo_mediciones/catalogo_mediciones.html', context)


def detalle_medicion(request, id):
    medicion = get_object_or_404(Tipo_alumbrado_art5, id=id)  # Obtener la medición
    context = {
        'medicion': medicion
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