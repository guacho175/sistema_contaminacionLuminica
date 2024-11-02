from django.urls import path
from . import views as v

urlpatterns = [

    path('mapa', v.mapa, name='mapa'),

]
