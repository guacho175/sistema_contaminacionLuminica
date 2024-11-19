from django.urls import path
from . import views as v


urlpatterns = [
    #path('', v.inicio, name=''),
    path('', v.cargar_fiscalizacion, name=''),
    path('fiscalizacionAdd/', v.crear_fiscalizacion, name='crear_fiscalizacion'),
    path('fiscalizacionDel/<int:fiscalizacion_id>/', v.eliminar_fiscalizacion, name='eliminarFiscalizacion'),
    path('fiscalizacion/<int:proyecto_id>/detalle/', v.detalle_fiscalizacion, name='detalleFiscalizacion'),
    path('medicionAdd/<int:fiscalizacion_id>/', v.nueva_medicion, name='nuevaMedicion'),




]
