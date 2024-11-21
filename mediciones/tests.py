from django.test import TestCase, RequestFactory
from services.mediciones.medicionCRUD import MedicionService
from mediciones.models import Medicion
from fiscalizacion.models import Fiscalizacion

class MedicionServiceTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.post('/')
        self.service = MedicionService(self.request)

    def test_crear_medicion(self):
        # Agrega pruebas para validar la creación de mediciones
        pass

    def test_eliminar_medicion(self):
        # Agrega pruebas para validar la eliminación de mediciones
        pass
