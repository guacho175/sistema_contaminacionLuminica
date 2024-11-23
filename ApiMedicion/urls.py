from django.urls import path
from . import views as v

urlpatterns = [
    #path('', v.inicio, name=''),
    path('ApiInstrumentoMedicion', v.ApiInstrumentoMedicion, name='ApiInstrumentoMedicion'),
    path('ApiProyecto', v.ApiProyecto, name='ApiProyecto'),
    path('ApiLogin', v.ApiLogin, name='ApiLogin'),


]