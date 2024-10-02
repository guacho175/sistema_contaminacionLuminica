from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo_mediciones/<str:codigo>/', v.catalogo_mediciones, name='catalogo_mediciones'),
    path('historial/<int:codigo>/', v.historial, name='historial'),
    path('areas/', v.areas_protegidas, name='areas'),

    
]
