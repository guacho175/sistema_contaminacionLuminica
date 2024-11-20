from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile


def validar_tamano_archivo(archivo, limite_mb):
    """
    Valida el tamaño de un archivo.
    :param archivo: Archivo a validar.
    :param limite_mb: Tamaño máximo permitido en MB.
    :raises ValidationError: Si el archivo excede el tamaño permitido.
    """
    if isinstance(archivo, UploadedFile) and archivo.size > limite_mb * 1024 * 1024:  
        raise ValidationError(f"El tamaño del archivo no debe superar los {limite_mb} MB.")
    return archivo