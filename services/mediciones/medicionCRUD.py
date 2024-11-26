from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import RestrictedError
from fiscalizacion.models import Fiscalizacion
from mediciones.models import Medicion

class MedicionCRUD:
    """Servicio para manejar operaciones relacionadas con mediciones."""

    def __init__(self, request):
        self.request = request

    def crear_medicion(self, fiscalizacion_id, form):
        """Crear una nueva medición asociada a una fiscalización."""
        fiscalizacion = get_object_or_404(Fiscalizacion, id=fiscalizacion_id)
        current_url = self.request.META.get('HTTP_REFERER', '/')
        
        if form.is_valid():
            medicion = form.save(commit=False)
            medicion.fiscalizacion = fiscalizacion
            medicion.save()
            messages.success(self.request, 'Medición ingresada correctamente.')
            return HttpResponseRedirect(current_url)
        
        return None, form, fiscalizacion

    def eliminar_medicion(self, medicion_id):
        """Eliminar una medición."""
        medicion = get_object_or_404(Medicion, id=medicion_id)

        if self.request.method == 'POST':
            try:
                medicion.delete()
                messages.success(self.request, f'La medición {medicion_id} se eliminó correctamente.')
            except RestrictedError as e:
                messages.error(self.request, f'No se puede eliminar la medición: {e.args[0]}')
            except Exception as e:
                messages.error(self.request, f'Error al eliminar la medición: {str(e)}')

        return medicion
