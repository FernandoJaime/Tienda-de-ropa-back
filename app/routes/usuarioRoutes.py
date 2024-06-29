from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..service.user_service import create_user, get_all_users
from ..utils.validators import validate_email, validate_password

# Definición del blueprint para gestionar rutas relacionadas con usuarios
setup_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

# Endpoint para la creación de un nuevo usuario
@setup_bp.route('/registro', methods=['POST'])
@jwt_required()  # Protegido por autenticación JWT
def create_user_endpoint():
    data = request.json

    # Validación de campos obligatorios en la solicitud
    if not all([data.get('nombre'), data.get('apellido'), data.get('fecha_nacimiento'),
                data.get('email'), data.get('password'), data.get('telefono'),
                data.get('nacionalidad'), data.get('domicilio')]):
        return jsonify({"msg": "Faltan datos"}), 400

    # Validación del formato del email
    if not validate_email(data.get('email')):
        return jsonify({"msg": "Email inválido"}), 400

    # Validación de la contraseña
    if not validate_password(data.get('password')):
        return jsonify({"msg": "Contraseña inválida"}), 400

    try:
        # Intentar crear un nuevo usuario usando el servicio correspondiente
        nuevo_usuario = create_user(data)
        return jsonify(nuevo_usuario.serialize()), 201  # Devolver el nuevo usuario creado
    except Exception as e:
        # Capturar cualquier excepción y devolver un mensaje de error adecuado
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500

# Endpoint para obtener todos los usuarios
@setup_bp.route('/listar', methods=['GET'])
@jwt_required()  # Protegido por autenticación JWT
def get_all_users_endpoint():
    try:
        # Intentar obtener todos los usuarios usando el servicio correspondiente
        users = get_all_users()
        return jsonify(users), 200  # Devolver la lista de usuarios
    except Exception as e:
        # Capturar cualquier excepción y devolver un mensaje de error adecuado
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500
