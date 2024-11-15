from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('mediciones/', include('historialMediciones.urls')),
    path('', include('fiscalizacion.urls')),
    path('', include('mediciones.urls')),
    path('', include('proyectos.urls')),
    path('', include('usuarios.urls')),

]
