from django.urls import path
from . import views as v


urlpatterns = [
    path('Login', v.api_login, name='Login'),
    path('Api_fiscalizaciones', v.cargar_fiscalizaciones_completas, name='cargar_proyectos_fiscalizaciones'),

]



