from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.inicio, name=''),
    path('catalogo_mediciones/<int:codigo>/<str:mes>/', v.catalogo_mediciones, name='catalogo_mediciones'),
    path('historial/<int:codigo>/', v.historial, name='historial'),
    path('areas/', v.areas_protegidas, name='areas'),
]
