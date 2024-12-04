from django.urls import path
from . import views as v


urlpatterns = [
    #path('', v.inicio, name=''),
    path('', v.iniciar_sesion, name='inicio'),  # Página de inicio
    path('logout/', v.cerrar_sesion, name='logout'),


    path('fiscalizaciones/', v.cargar_fiscalizaciones, name=''),
    path('fiscalizacionAdd/', v.crear_fiscalizacion, name='crear_fiscalizacion'),
    path('fiscalizacionDel/<int:fiscalizacion_id>/', v.eliminar_fiscalizacion, name='eliminarFiscalizacion'),
    path('fiscalizacion/<int:fiscalizacion_id>/detalle/', v.detalle_fiscalizacion, name='detalleFiscalizacion'),
]
