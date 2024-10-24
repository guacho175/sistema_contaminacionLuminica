from django.contrib import admin
from .models import Usuario, Rol, TipoAlumbradoArt5, TipoAlumbradoArt6, CatalogoMedicion

# Register your models here.
admin.site.register(TipoAlumbradoArt5)
admin.site.register(TipoAlumbradoArt6)
admin.site.register(CatalogoMedicion)

admin.site.register(Usuario)
admin.site.register(Rol)