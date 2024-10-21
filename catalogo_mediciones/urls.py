from django.urls import path
from . import views as v


urlpatterns = [

    path('', v.catalogo_mediciones, name='catalogo'),
    path('catalogo/detalle/<int:id>/', v.detalle_medicion, name='detalle_medicion'),
    path('medicion/<int:id>/editar/', v.editar_medicion, name='editar_medicion'),
]
