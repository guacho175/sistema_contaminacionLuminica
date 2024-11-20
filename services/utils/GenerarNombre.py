import os
from django.utils import timezone


class GenerarNombre:
    @staticmethod
    def generar_nombre(instance, filename):
        """
        Genera un nombre único para un archivo basado en la fecha y hora actuales.
        """
        if not isinstance(filename, str):  # Verifica si 'filename' no es un string
            raise ValueError("El argumento filename debe ser una cadena de texto.")

        extension = os.path.splitext(filename)[1]  # Extrae la extensión incluyendo el punto
        ruta = 'proyectos'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")  # Fecha y hora en formato deseado
        nombre = f"{fecha}{extension}"  # Construye el nombre del archivo
        return os.path.join(ruta, nombre)


