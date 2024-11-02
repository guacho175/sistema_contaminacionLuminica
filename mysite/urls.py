from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('mediciones/', include('historialMediciones.urls')),
    path('', include('historialMediciones.urls')),
    path('', include('mapa.urls')),
    path('', include('catalogo_mediciones.urls')),
    path('', include('proyectos.urls')),
    path('', include('inspectores.urls')),

]
