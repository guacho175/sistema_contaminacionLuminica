from django.urls import path
from . import views as v


urlpatterns = [
    path('catalogoMedicion/', v.cargar_medicion, name='catalogoMedicion')


]
