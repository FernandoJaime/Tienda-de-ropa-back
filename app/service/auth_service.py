from werkzeug.security import check_password_hash
from ..models.usuario import Usuario



"""
    Autentica al usuario verificando las credenciales proporcionadas.

    - email (str): Correo electrónico del usuario.
    - password (str): Contraseña del usuario en texto plano.

    Retorna:
    - Usuario: Objeto Usuario si la autenticación es exitosa y el usuario tiene rol 'empleado'.
              None si las credenciales son inválidas o el usuario no tiene el rol adecuado.
"""
def authenticate_user(email, password):
    # Buscar usuario por email en la base de datos
    user = Usuario.find_by_email(email)  
    if user and check_password_hash(user.password, password):
        # Verificar si la contraseña proporcionada coincide con la almacenada
        if user.rol == 'empleado':
            # Devolver el objeto Usuario si es un empleado
            return user  
    # Devolver None si no se encontró el usuario o no tiene el rol correcto        
    return None  


"""
    Genera un token JWT para el usuario dado.

    - user (Usuario): Objeto Usuario para el cual se generará el token JWT.

    Retorna:
    - str: Token JWT generado.
"""
def generate_jwt(user):
    return user.generate_jwt()  
# Llamar al método generate_jwt() del objeto Usuario para generar el token
