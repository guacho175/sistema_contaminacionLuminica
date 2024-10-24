from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicionForm
from .models import TipoAlumbradoArt5, TipoAlumbradoArt6, CatalogoMedicion
import folium
from folium.plugins import MarkerCluster


def catalogo_mediciones(request):
    catalogo_mediciones = CatalogoMedicion.objects.all()
    mediciones_art5 = TipoAlumbradoArt5.objects.all()
    mediciones_art6 = TipoAlumbradoArt6.objects.all()

    # Crear el mapa
    initialMap = folium.Map(location=[-29.9055324, -71.2313308], zoom_start=11) #, tiles='CartoDB dark_matter'
    marker_cluster = MarkerCluster().add_to(initialMap)

    # Iterar sobre las mediciones del catálogo
    for medicion in catalogo_mediciones:
        # Condicional para las mediciones de art5
        if medicion.medicion_art5:
            lat = medicion.medicion_art5.latitud
            lng = medicion.medicion_art5.longitud
            direccion = medicion.medicion_art5.direccion
            nivel_cumpl = medicion.medicion_art5.nivel_cumplimiento
            tipo = "Art 5"
            usuario = medicion.medicion_art5.usuario
        # Condicional para las mediciones de art6
        elif medicion.medicion_art6:
            lat = medicion.medicion_art6.latitud
            lng = medicion.medicion_art6.longitud
            direccion = medicion.medicion_art6.direccion
            nivel_cumpl = medicion.medicion_art6.nivel_cumplimiento
            tipo = "Art 6"
            usuario = medicion.medicion_art6.usuario

        # Determinar el icono según el nivel de cumplimiento
        if nivel_cumpl == '0':
            icon = folium.Icon(icon="minus-sign", prefix="glyphicon", color="gray")
        elif nivel_cumpl == '1':
            icon = folium.Icon(icon="remove-sign", prefix="glyphicon", color="red")
        elif nivel_cumpl == '2':
            icon = folium.Icon(icon="ok-sign", prefix="glyphicon", color="orange")
        else:
            icon = folium.Icon(icon="ok-sign", prefix="glyphicon", color="green")

        # Agregar el marcador al cluster
        folium.Marker(
            location=[lat, lng],
            popup=f'{direccion} ({tipo}) - Inspector: {usuario}',
            tooltip=f'{direccion} - Nivel de Cumplimiento: {nivel_cumpl}',
            icon=icon
        ).add_to(marker_cluster)

    context = {
        'catalogo_mediciones': catalogo_mediciones,
        'mediciones_art5': mediciones_art5,
        'mediciones_art6': mediciones_art6,
        'map': initialMap._repr_html_()  # El mapa se pasa como HTML
    }

    return render(request, 'catalogo_mediciones/catalogo_mediciones.html', context)


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
                medicion_art5.estado = 1  # Cambia el estado
                medicion_art5.save()  # Guarda el cambio
            elif medicion_art6:
                nueva_medicion_catalogo.medicion_art6 = medicion_art6
                medicion_art6.estado = 1  # Cambia el estado
                medicion_art6.save()  # Guarda el cambio

            nueva_medicion_catalogo.save()  # Guardar en el catálogo

            # Redirigir al catálogo después de guardar
            return redirect('catalogo')
    else:
        form = MedicionForm()

    return render(request, 'catalogo_mediciones/registrar_medicion.html', {'form': form})


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
