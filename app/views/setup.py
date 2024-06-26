from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from ..models.usuario import Usuario 

# Crear un blueprint llamado 'setup' con prefijo de URL '/setup'
setup_bp = Blueprint('setup', __name__, url_prefix='/setup')


"""
    Endpoint para crear un nuevo usuario.

    Recibe datos JSON desde la solicitud POST con los siguientes campos requeridos:
    - nombre (str)
    - apellido (str)
    - fecha_nacimiento (str en formato YYYY-MM-DD)
    - email (str)
    - password (str)
    - telefono (str)
    - nacionalidad (str)
    - domicilio (str)
    
    Opcional:
    - rol (str): Por defecto es 'cliente' si no se especifica.

    Retorna:
    - JSON con mensaje de éxito si el usuario se crea correctamente.
    - JSON con mensaje de error y código de estado 400 si faltan datos requeridos.
"""
@setup_bp.route('/create', methods=['POST'])
def create_user():
    
    # Obtener datos del JSON enviado en la solicitud
    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')
    fecha_nacimiento = request.json.get('fecha_nacimiento')
    email = request.json.get('email')
    password = request.json.get('password')
    telefono = request.json.get('telefono')
    nacionalidad = request.json.get('nacionalidad')
    domicilio = request.json.get('domicilio')
    # Por defecto, el rol es 'cliente' si no se especifica
    rol = request.json.get('rol', 'cliente')  

    # Verificar que todos los campos requeridos estén presentes
    if not all([nombre, apellido, fecha_nacimiento, email, password, telefono, nacionalidad, domicilio]):
        return jsonify({"msg": "Faltan datos"}), 400

    # Transformar nombre, apellido y rol a formato capitalize
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    rol = rol.capitalize()
    nacionalidad = nacionalidad.capitalize()
    domicilio = domicilio.capitalize()

    # Generar hash de la contraseña
    hashed_password = generate_password_hash(password)

    # Crear instancia de Usuario
    nuevo_usuario = Usuario(
        nombre=nombre,
        apellido=apellido,
        fecha_nacimiento=fecha_nacimiento,
        email=email,
        password=hashed_password,
        telefono=telefono,
        nacionalidad=nacionalidad,
        domicilio=domicilio,
        rol=rol
    )
    
    # Guardar el usuario en la base de datos
    nuevo_usuario.save()

    # Respuesta exitosa
    return jsonify({"msg": "Usuario creado exitosamente"}), 201



"""
    Endpoint para obtener todos los usuarios registrados en la base de datos.

    Retorna:
    - JSON con la lista de todos los usuarios serializados y código de estado 200 si se obtienen correctamente.
    - JSON con mensaje de error y código de estado 500 si ocurre algún problema al obtener los usuarios.
"""
@setup_bp.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = Usuario.get_all_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"msg": f"Error al obtener usuarios: {str(e)}"}), 500
