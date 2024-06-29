from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
import jwt
from ..database import get_db
import os

class Usuario:
    
    #Representa un usuario del sistema con métodos para autenticación, gestión de JWT, operaciones de base de datos y serialización.


    def __init__(self, nombre, apellido, fecha_nacimiento, email, password, telefono, nacionalidad, domicilio, rol, id=None):
        # Inicializa un objeto Usuario con los atributos especificados.
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
     Authenticate(email, password): Método estático para autenticar a un usuario por email y contraseña.
    Returns:
        - str: Token JWT si la autenticación es exitosa y el usuario tiene rol 'empleado', None en caso contrario.
    """
    @staticmethod
    def authenticate(email, password):
        user = Usuario.find_by_email(email)
        if user and check_password_hash(user.password, password):
            if user.rol == 'empleado':
                return user.generate_jwt()
        return None


    """
    generate_jwt(): Genera un token JWT para el usuario actual.
        Genera un token JWT para el usuario actual.
    """
    def generate_jwt(self):
        payload = {
            'sub': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'rol': self.rol,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        return jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), algorithm='HS256')


    """
    find_by_email(email): Método estático para buscar un usuario por su email en la base de datos.
        urns:
        - Usuario: Objeto Usuario si se encuentra en la base de datos, None si no se encuentra.
    """
    @staticmethod
    def find_by_email(email):
        # Busca un usuario por su email en la base de datos.
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
    save(): Guarda el usuario actual en la base de datos.
    """   
    def save(self):
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, email, password, telefono, nacionalidad, domicilio, rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (self.nombre, self.apellido, self.fecha_nacimiento, self.email, self.password, self.telefono, self.nacionalidad, self.domicilio, self.rol))
        db.commit()
        cursor.close()
        
        
    """
    serialize(): Retorna una representación serializada del usuario en forma de diccionario.
        Retorna una representación serializada del usuario en forma de diccionario.
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
    get_all_users(): Método estático que obtiene todos los usuarios almacenados en la base de datos.
        Retorna una lista de todos los usuarios alamacenados en la db, 
        de los usuarios serializados como dicionario por la funcion (serialize)
    """
    @staticmethod
    def get_all_users():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = "SELECT id, nombre, apellido, fecha_nacimiento, email, telefono, nacionalidad, domicilio, rol FROM usuarios"
        cursor.execute(query)
        rows = cursor.fetchall()
        users = [Usuario(id=row['id'], nombre=row['nombre'], apellido=row['apellido'], fecha_nacimiento=row['fecha_nacimiento'],
                         email=row['email'], password=None, telefono=row['telefono'], nacionalidad=row['nacionalidad'],
                         domicilio=row['domicilio'], rol=row['rol']).serialize() for row in rows]
        cursor.close()
        return users
