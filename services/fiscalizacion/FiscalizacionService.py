from typing import List, Dict, Tuple
from django.db.models import Min, Max, Avg
from fiscalizacion.models import Fiscalizacion
from proyectos.models import Proyecto
from usuarios.models import Usuario
from mediciones.models import Medicion

class FiscalizacionService:
    """Servicio para manejar operaciones relacionadas con las fiscalizaciones."""

    @staticmethod
    def crear_fiscalizacion(proyecto_id: int, usuario_id: int, foto) -> None:
        proyecto = Proyecto.objects.get(id=proyecto_id)
        usuario = Usuario.objects.get(id=usuario_id)
        fiscalizacion = Fiscalizacion(proyecto=proyecto, usuario=usuario, foto=foto)
        fiscalizacion.save()

    @staticmethod
    def cargar_fiscalizaciones() -> List[Fiscalizacion]:
        fiscalizaciones = Fiscalizacion.objects.all()
        return fiscalizaciones

    @staticmethod
    def detalle_fiscalizacion(fiscalizacion_id: int) -> Fiscalizacion:
        return Fiscalizacion.objects.get(id=fiscalizacion_id)

    @staticmethod
    def eliminar_fiscalizacion(fiscalizacion_id: int) -> None:
        fiscalizacion = Fiscalizacion.objects.get(id=fiscalizacion_id)
        fiscalizacion.delete()

    @staticmethod
    def obtener_mediciones(fiscalizacion_id: int) -> List[Medicion]:
        fiscalizacion = Fiscalizacion.objects.get(id=fiscalizacion_id)
        return list(fiscalizacion.mediciones.all())
