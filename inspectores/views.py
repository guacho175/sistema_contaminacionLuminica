from django.shortcuts import render
from .models import Inspector

# Create your views here.
def cargar_inspector(request):
    inspectores = Inspector.objects.all()
    
    data = {
        'inspectores': inspectores
    }
    return render(request, 'inspectores/mantenedor_inspectores.html', data)