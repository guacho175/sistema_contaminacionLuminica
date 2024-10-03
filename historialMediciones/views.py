from django.shortcuts import render
from .models import areas_protegidas as areas

def catalogo_mediciones(request, codigo, mes):
    area = areas.get(codigo)
    
    if area:
        mediciones_mensuales = area.get('mediciones_mensuales_2024', {})
        datos_mes = mediciones_mensuales.get(mes, {})
        data = {
            'area': area,
            'mes': mes,
            'datos_mes': datos_mes,
        }
    else:
        data = {'error': 'Área protegida no encontrada.'}
    
    return render(request, 'historialMediciones/catalogo_mediciones.html', data)

def historial(request, codigo):
    area = areas.get(codigo)
    
    if area:
        data = {
            'area': area,
            'codigo': codigo, 
            'mediciones_mensuales': area.get('mediciones_mensuales_2024', {}),
        }
    else:
        data = {'error': 'Área protegida no encontrada.'}
    
    return render(request, 'historialMediciones/historial.html', data)

def areas_protegidas(request):
    data = {
        'areas': areas,
    }
    return render(request, 'historialMediciones/areas_protegidas.html', data)
