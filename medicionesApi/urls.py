from django.urls import path
from . import views as v


urlpatterns = [

    path('Api_mediciones', v.cargar_mediciones_completas, name='Api_mediciones'),

]



