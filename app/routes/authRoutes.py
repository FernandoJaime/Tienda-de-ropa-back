from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
import mysql.connector
from ..service.auth_service import authenticate_user, generate_jwt


# Definición del blueprint para las rutas de autenticación
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Conjunto para almacenar tokens JWT revocados
blacklist = set()


"""
Endpoint para iniciar sesión de usuario.

    Métodos permitidos:
    - POST

    Parámetros JSON requeridos:
    - email (str): Correo electrónico del usuario.
    - password (str): Contraseña del usuario.
    
    Respuestas:
    - 200 OK: Inicio de sesión exitoso. Devuelve un token de acceso JWT y un mensaje de éxito.
    - 400 Bad Request: Falta el email o la contraseña en la solicitud JSON.
    - 401 Unauthorized: Credenciales incorrectas.
    - 500 Internal Server Error: Error interno del servidor.
"""
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return jsonify({"msg": "Email y contraseña son requeridos"}), 400

        user = authenticate_user(email, password)

        if not user:
            return jsonify({"msg": "Credenciales incorrectas"}), 401

        access_token = generate_jwt(user)
        return jsonify(access_token=access_token, msg="Inicio de sesión exitoso"), 200

    except Exception as e:
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500
    
    
    
"""
Endpoint para cerrar sesión de usuario.

    Métodos permitidos:
    - POST

    Requiere JWT en el encabezado Authorization.

    Respuestas:
    - 200 OK: Cierre de sesión exitoso. Agrega el token JWT a la lista negra.
    - 400 Bad Request: Token JWT inválido.
    - 500 Internal Server Error: Error interno del servidor o error de base de datos.
"""
@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    try:
        jti = get_jwt()['jti']
        blacklist.add(jti)
        return jsonify({"msg": "Cierre de sesión exitoso"}), 200
    except mysql.connector.Error as db_error:
        return jsonify({"msg": f"Error en la base de datos: {db_error}"}), 500
    except KeyError:
        return jsonify({"msg": "Token JWT inválido"}), 400
    except Exception as e:
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500
