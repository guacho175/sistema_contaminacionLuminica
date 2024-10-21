from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Tipo_alumbrado_art5
from django.views.generic.edit import UpdateView


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

class MedicionUpdateView(UpdateView):
    model = Tipo_alumbrado_art5
    fields = [
        'direccion', 'latitud', 'longitud', 'tipo', 'menor_igual_90grados', 
        'mayor_90grados', 'clase_luminaria', 'emision_reflexion', 
        'proteccion_especial', 'radiancia_espectral', 'emision_conjunta', 
        'usuario','nivel_cumplimiento','observaciones'
    ]
    template_name = 'catalogo_mediciones/editar_medicion.html'
    success_url = reverse_lazy('catalogo')