from werkzeug.security import generate_password_hash
from ..models.usuario import Usuario



"""
    Crea un nuevo usuario a partir de los datos proporcionados.

    Args:
    - data (dict): Diccionario con los datos del usuario a crear.
      Debe contener los siguientes campos:
      - 'nombre': Nombre del usuario.
      - 'apellido': Apellido del usuario.
      - 'fecha_nacimiento': Fecha de nacimiento del usuario.
      - 'email': Correo electrónico del usuario.
      - 'password': Contraseña en texto plano del usuario.
      - 'telefono': Número de teléfono del usuario.
      - 'nacionalidad': Nacionalidad del usuario.
      - 'domicilio': Domicilio del usuario.
      - 'rol' (opcional): Rol del usuario (por defecto 'cliente').

    Retorna:
    - Usuario: Objeto Usuario creado y almacenado en la base de datos.
"""
def create_user(data):
    # Capitalizar nombres y nacionalidad para uniformidad
    nombre = data.get('nombre').capitalize()
    apellido = data.get('apellido').capitalize()
    fecha_nacimiento = data.get('fecha_nacimiento')
    email = data.get('email')
    password = generate_password_hash(data.get('password'))  # Generar hash de la contraseña
    telefono = data.get('telefono')
    nacionalidad = data.get('nacionalidad').capitalize()
    domicilio = data.get('domicilio').capitalize()
    rol = data.get('rol', 'cliente').capitalize()  # Rol por defecto 'cliente'

    # Crear instancia de Usuario con los datos proporcionados
    nuevo_usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        fecha_nacimiento=fecha_nacimiento,
        email=email,
        password=password,
        telefono=telefono,
        nacionalidad=nacionalidad,
        domicilio=domicilio,
        rol=rol
    )

    nuevo_usuario.save()  # Guardar el nuevo usuario en la base de datos
    return nuevo_usuario  # Devolver el objeto Usuario creado


"""
    Obtiene todos los usuarios almacenados en la base de datos.

    Retorna:
    - list: Lista de objetos Usuario.
"""
def get_all_users():
    return Usuario.get_all_users()  # Llamar al método estático de Usuario para obtener todos los usuarios
