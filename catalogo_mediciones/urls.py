from django.urls import path
from . import views as v
from .views import MedicionUpdateView


urlpatterns = [

    path('', v.catalogo_mediciones, name='catalogo'),
    path('catalogo/detalle/<int:id>/', v.detalle_medicion, name='detalle_medicion'),
    path('medicion/<int:pk>/editar/', MedicionUpdateView.as_view(), name='editar_medicion'),



]
