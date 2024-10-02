from django.shortcuts import render
from .models import areas_protegidas as areas

# Create your views here.
def catalogo_mediciones(request, codigo):
    areas_protegidas = areas # Obtener el área protegida específica usando el código
    area = areas_protegidas.get(codigo)
    
    # Verificar si existe el área protegida
    if area:
        data = {
            'area': area,
            'mediciones_mensuales': area['mediciones_mensuales_2024'],
        }
    else:
        data = {'error': 'Área protegida no encontrada.'}
    return render(request, 'historialMediciones/catalogo_mediciones.html', data)


def historial(request, codigo):
    areas_protegidas = areas # Obtener el área protegida específica usando el código
    area = areas_protegidas.get(codigo)
    
    # Verificar si existe el área protegida
    if area:
        data = {
            'area': area,
            'mediciones_mensuales': area['mediciones_mensuales_2024'],
        }
    else:
        data = {'error': 'Área protegida no encontrada.'}
    return render(request, 'historialMediciones/historial.html', data)


def areas_protegidas(request):
    data = {
        'areas': areas,
    }
    return render(request, 'historialMediciones/areas_protegidas.html', data)



