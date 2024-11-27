from django.urls import path
from . import views as v


urlpatterns = [

    path('api_cargos', v.cargar_cargos, name='Api_cargos'),
    path('api_instituciones', v.cargar_instituciones, name='Api_instituciones'),
    path('api_personas', v.cargar_personas, name='api_personas'),
    path('api_usuarios', v.cargar_usuarios, name='api_usuarios'),
    path('api_usuarios', v.cargar_usuarios_completos, name='api_usuarios'),

]



