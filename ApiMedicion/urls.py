from django.urls import path
from . import views as v

urlpatterns = [
    #path('', v.inicio, name=''),
    path('api_instrumentos_medicion', v.cargar_instrumento_medicion, name='api_instrumentos_medicion'),
    path('api_mediciones', v.cargar_medicion, name='api_mediciones'),




    path('api_login', v.api_login, name='api_login'),
    path('api_cargos', v.cargar_cargo, name='api_cargos'),
    path('api_instituciones', v.cargar_institucion, name='cargar_instituciones'),
    path('api_usuarios', v.cargar_usuario, name='api_usuarios'),




    path('api_proyecto', v.cargar_proyecto, name='api_proyecto'),
    path('api_titular', v.cargar_titular, name='api_titular'),
    path('api_representante_legal', v.cargar_representante_legal, name='api_representante_legal'),
    path('api_detalle_luminaria', v.cargar_detalle_luminaria, name='api_detalle_luminaria'),
    
    path('api_modelo_proyecto', v.cargar_modelo_proyecto, name='api_modelo_proyecto'),




    path('api_fiscalizacion', v.cargar_fiscalizacion, name='api_fiscalizacion'),



]