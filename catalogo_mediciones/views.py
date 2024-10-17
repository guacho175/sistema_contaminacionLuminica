from django.shortcuts import render

# Create your views here.
def catalogo_mediciones(request):
    context = {}
    return render(request, 'catalogo_mediciones/catalogo_mediciones.html', context)