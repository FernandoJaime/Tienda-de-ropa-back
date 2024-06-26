from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
import jwt

from app.database import get_db

class Usuario:
    """
    Clase que representa a un usuario del sistema.
    """
    def __init__(self, nombre, apellido, fecha_nacimiento, email, password, telefono, nacionalidad, domicilio, rol, id=None):
        """
        Inicializa un nuevo objeto Usuario con los atributos proporcionados.

        Args:
        - nombre (str): Nombre del usuario.
        - apellido (str): Apellido del usuario.
        - fecha_nacimiento (str): Fecha de nacimiento del usuario en formato YYYY-MM-DD.
        - email (str): Correo electrónico del usuario.
        - password (str): Contraseña del usuario (almacenada como hash).
        - telefono (str): Número de teléfono del usuario.
        - nacionalidad (str): Nacionalidad del usuario.
        - domicilio (str): Domicilio del usuario.
        - rol (str): Rol del usuario ('empleado', 'cliente', etc.).
        - id (int, opcional): Identificador único del usuario en la base de datos.
        """
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.email = email
        self.password = password
        self.telefono = telefono
        self.nacionalidad = nacionalidad
        self.domicilio = domicilio
        self.rol = rol


    """
        Funcion autenticate(email, password)
        Verifica las credenciales del usuario y devuelve el objeto Usuario si las credenciales son correctas.

        Args:
        - email (str): Correo electrónico del usuario.
        - password (str): Contraseña del usuario (sin cifrar).

        Returns:
        - Usuario: Objeto Usuario si las credenciales son válidas y el rol es 'empleado', None en caso contrario.
    """
    @staticmethod
    def authenticate(email, password):
        user = Usuario.find_by_email(email)
        if user and check_password_hash(user.password, password):
            if user.rol == 'empleado':
                return user
        return None



    """
        Funcion generate_jwt(self)
        Genera un token JWT (JSON Web Token) con información del usuario.

        Returns:
        - str: Token JWT codificado.
    """
    def generate_jwt(self):
        payload = {
            'usuario_id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'rol': self.rol,
            # Expira en 1 hora desde ahora
            'exp': datetime.utcnow() + timedelta(hours=1)  
        }
        return jwt.encode(payload, 'JWT_SECRET_KEY', algorithm='HS256')



    """
        Funcion find_by_email(email)
        Busca un usuario por su correo electrónico en la base de datos y devuelve un objeto Usuario si lo encuentra.

        Args:
        - email (str): Correo electrónico del usuario.

        Returns:
        - Usuario or None: Objeto Usuario si se encuentra en la base de datos, None si no se encuentra.
    """
    @staticmethod
    def find_by_email(email):
        query = "SELECT id, nombre, apellido, fecha_nacimiento, email, telefono, nacionalidad, domicilio, rol, password FROM usuarios WHERE email = %s"
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(query, (email,))
        user_data = cursor.fetchone()
        cursor.close()
        if user_data:
            return Usuario(**user_data)
        else:
            return None
    
    
    """
        Funcion save(self)
        Guarda el usuario en la base de datos.
    """
    def save(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, email, password, telefono, nacionalidad, domicilio, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (self.nombre, self.apellido, self.fecha_nacimiento, self.email, self.password, self.telefono, self.nacionalidad, self.domicilio, self.rol))
        db.commit()
        cursor.close()


    """
        Funcion serialize(self)
        Devuelve una representación serializada del usuario en forma de diccionario.

        Returns:
        - dict: Diccionario con los datos del usuario serializados.
    """
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'fecha_nacimiento': self.fecha_nacimiento,
            'email': self.email,
            'telefono': self.telefono,
            'nacionalidad': self.nacionalidad,
            'domicilio': self.domicilio,
            'rol': self.rol
        }



    """
        Funcion get_all_users()
        Obtiene todos los usuarios registrados en la base de datos y los devuelve como una lista de diccionarios serializados.

        Returns:
        - list: Lista de diccionarios con los datos de todos los usuarios serializados.
    """
    @staticmethod
    def get_all_users():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = "SELECT id, nombre, apellido, fecha_nacimiento, email, telefono, nacionalidad, domicilio, rol FROM usuarios"
        cursor.execute(query)
        rows = cursor.fetchall()

        users = [
            Usuario(
                id=row['id'],
                nombre=row['nombre'],
                apellido=row['apellido'],
                fecha_nacimiento=row['fecha_nacimiento'],
                email=row['email'],
                # No incluir la contraseña en la serialización
                password=None,  
                telefono=row['telefono'],
                nacionalidad=row['nacionalidad'],
                domicilio=row['domicilio'],
                rol=row['rol']
                # Serializar cada usuario y agregarlo a la lista
            ).serialize()  
            for row in rows
        ]

        cursor.close()
        return users
