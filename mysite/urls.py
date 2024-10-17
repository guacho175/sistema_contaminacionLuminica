from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('mediciones/', include('historialMediciones.urls')),
    path('', include('historialMediciones.urls')),
    path('mapa/', include('mapa.urls')),
    path('catalogo/', include('catalogo_mediciones.urls')),

]
