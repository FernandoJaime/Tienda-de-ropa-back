import re


"""
    Valida si un correo electrónico tiene un formato válido.

    - email (str): Correo electrónico a validar.

    Retorna:
    - bool: True si el correo electrónico es válido, False si no lo es.
"""
def validate_email(email):
    email_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'  # Expresión regular para validar el formato del email
    if re.match(email_regex, email):
        return True
    return False

"""
    Valida si una contraseña cumple con los requisitos mínimos.

    - password (str): Contraseña a validar.

    Retorna:
    - bool: True si la contraseña cumple con los requisitos, False si no.
    """
def validate_password(password):
    # Verificar que la longitud de la contraseña sea al menos de 8 caracteres
    return len(password) >= 8
