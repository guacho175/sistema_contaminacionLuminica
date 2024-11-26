import os
from django.utils import timezone


class GenerarNombre:
    @staticmethod
    def generar_nombre(instance, filename, ruta):
        """
        Genera un nombre único para un archivo basado en la fecha y hora actuales.
        :param instance: La instancia del modelo asociado al archivo.
        :param filename: Nombre del archivo original.
        :param ruta: Ruta base para almacenar el archivo.
        :return: Ruta completa con un nombre único para el archivo.
        """
        if not isinstance(filename, str):  # Verifica si 'filename' no es un string
            raise ValueError("El argumento filename debe ser una cadena de texto.")

        extension = os.path.splitext(filename)[1]  # Extrae la extensión incluyendo el punto
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")  # Fecha y hora en formato deseado
        nombre = f"{fecha}{extension}"  # Construye el nombre del archivo
        return os.path.join(ruta, nombre)

    @staticmethod
    def generar_nombre_fiscalizacion(instance, filename):
        """
        Genera un nombre único para archivos en la carpeta 'fiscalizacion'.
        """
        return GenerarNombre.generar_nombre(instance, filename, ruta='fiscalizacion')


    @staticmethod
    def generar_nombre_medicion(instance, filename):
        """
        Genera un nombre único para archivos en la carpeta 'medicion'.
        """
        return GenerarNombre.generar_nombre(instance, filename, ruta='medicion')
