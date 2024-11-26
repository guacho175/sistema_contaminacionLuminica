from django.urls import path
from . import views as v


urlpatterns = [

    path('Api_fiscalizaciones', v.cargar_fiscalizaciones_completas, name='cargar_proyectos_fiscalizaciones'),

]



