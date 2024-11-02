from django.urls import path
from . import views as v


urlpatterns = [
    path('inspectores/', v.cargar_inspector, name='inspectores'),

]
