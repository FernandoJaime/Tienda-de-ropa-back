

"""
    Formatea un objeto datetime según el formato especificado.

    - dt (datetime): Objeto datetime que se desea formatear.
    - format (str, optional): Formato deseado para la representación del datetime.
      Por defecto, el formato es '%Y-%m-%d %H:%M:%S'.

    Retorna:
    - str: Representación formateada del datetime según el formato especificado.
    """
def format_datetime(dt, format='%Y-%m-%d %H:%M:%S'):
    return dt.strftime(format)

