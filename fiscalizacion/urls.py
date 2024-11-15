from django.urls import path
from . import views as v


urlpatterns = [
    #path('', v.inicio, name=''),
    path('', v.cargar_fiscalizacion, name=''),


]
