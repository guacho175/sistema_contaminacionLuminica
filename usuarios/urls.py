from django.urls import path
from . import views as v


urlpatterns = [
    path('usuarios/', v.cargar_usuario, name='usuarios'),

]
