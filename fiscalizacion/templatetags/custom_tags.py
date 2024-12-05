from django import template

register = template.Library()

@register.filter
def has_perm(user, perm_name):
    """
    Verifica si el usuario tiene un permiso específico.
    
    Args:
        user: El usuario a verificar.
        perm_name: El nombre del permiso (e.g., 'app_label.permission_name').
    
    Returns:
        bool: True si el usuario tiene el permiso, False en caso contrario.
    """
    try:
        return user.has_perm(perm_name)
    except AttributeError:
        # Esto cubre casos en los que user es None o no es un usuario válido
        return False
