from django.contrib import admin
from .models import Tipo_alumbrado_art5, Usuario, Rol, Tipo_alumbrado_art6, CatalogoMedicion

# Register your models here.
admin.site.register(Tipo_alumbrado_art5)
admin.site.register(Tipo_alumbrado_art6)
admin.site.register(CatalogoMedicion)

admin.site.register(Usuario)
admin.site.register(Rol)