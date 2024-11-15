from django.urls import path
from . import views as v


urlpatterns = [
    path('mediciones/', v.cargar_medicion, name='mediciones'),
    path('medicionAdd/', v.crear_medicion, name='crearMedicion'),
    path('medicionDel/<int:medicion_id>/', v.eliminar_medicion, name='eliminarMedicion')
]
