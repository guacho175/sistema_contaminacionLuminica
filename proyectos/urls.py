from django.urls import path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('proyectoAdd/', v.crear_proyecto, name='crearProyecto'),
    path('proyectos/', v.cargar_proyecto, name='proyectos'),
    path('proyectoDel/<int:proyecto_id>/', v.eliminar_proyecto, name='eliminarProyecto'),
    path('proyectoEdit/<int:proyecto_id>', v.cargar_editar_proyecto, name='editarProyecto'),
    path('proyectoEditado/<int:proyecto_id>', v.editar_proyecto, name='proyectoEditado'),
]
