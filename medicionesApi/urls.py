from django.urls import path
from . import views as v


urlpatterns = [

    path('Api_mediciones', v.cargar_mediciones_completas, name='Api_mediciones'),
    path('Api_instrumentos_medicion', v.cargar_instrumentos_medicion, name='cargar_instrumentos_medicion'),
    path('Guardar_medicion', v.guardar_medicion, name='guardar_medicion'),
    path('Guardar_sensor', v.guardar_sensor, name='guardar_medicion'),



]



