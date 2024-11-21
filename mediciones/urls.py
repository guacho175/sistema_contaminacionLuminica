from django.urls import path
from . import views as v


urlpatterns = [
    path('medicionAdd/<int:fiscalizacion_id>/', v.nueva_medicion, name='nuevaMedicion'),
    path('medicionDel/<int:medicion_id>/', v.eliminar_medicion, name='eliminarMedicion')
]
