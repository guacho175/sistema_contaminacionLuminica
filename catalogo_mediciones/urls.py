from django.urls import path
from . import views as v


urlpatterns = [
    path('catalogoMedicion/', v.cargar_medicion, name='catalogoMedicion'),
    path('medicionAdd/', v.crear_medicion, name='crearMedicion'),
    path('medicionDel/<int:medicion_id>/', v.eliminar_medicion, name='eliminarMedicion')


]
