from django.urls import path
from . import views as v


urlpatterns = [

    path('Api_Proyectos', v.cargar_proyectos_completos, name='cargar_proyectos_completos'),
    path('Guardar_foto_proyecto', v.guardar_foto_proyecto, name='guardar_foto_proyecto'),



]



