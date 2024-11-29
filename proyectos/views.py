from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import  RestrictedError
from .models import Proyecto
from .forms import ProyectoForm


def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'El proyecto se ingreso correctamente.')
            return redirect('/proyectos/')
    else:
        form = ProyectoForm()

    # retornamos el formulario
    return render(request, 'proyectos/proyectoAdd.html', {'form':form})


def cargar_proyecto(request):
    proyectos = Proyecto.objects.all()
    
    data = {
        'proyectos': proyectos
    }
    return render(request, 'proyectos/mantenedor_proyectos.html', data)


def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        try:
            proyecto.delete()
            messages.success(request, 'El proyecto se eliminó correctamente.')
            return redirect('/proyectos/')
        except RestrictedError as e:
            messages.error(request, f'No se puede eliminar el proyecto porque está siendo referenciado en otro objeto: {e.args[0]}')

    return render(request, 'proyectos/proyectoDel.html', {'proyecto': proyecto})


def cargar_editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    form = ProyectoForm(instance=proyecto)
    
    return render(request, 'proyectos/proyectoEdit.html', {'form':form, 'proyecto':proyecto})


def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES, instance=proyecto)
        if form.is_valid():
            if 'foto' in request.FILES:
                proyecto.foto = request.FILES['foto'] # Asignamos imagen

            form.save()
            messages.success(request, 'El proyecto se modifico correctamente.')

            return redirect('/proyectos/')
        
        else:
            if 'foto' in form.errors:
                messages.warning(request, form.errors['foto'][0])  # Muestra el primer error relacionado con 'foto'
                return redirect(f'/proyectoEdit/{proyecto_id}')

    else:
        form = ProyectoForm(instance=proyecto)
    
    return render(request, 'proyectos/mantenedor_proyectos.html', {'form':form})