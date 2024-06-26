from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import mysql.connector

from ..models.usuario import Usuario

# Creación del blueprint para las rutas de autenticación
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')



"""
    Endpoint para iniciar sesión de usuarios.

    Recibe los datos de inicio de sesión (email y contraseña) desde el cuerpo de la solicitud JSON.
    Verifica las credenciales y genera un token JWT si son válidas.

    Returns:
    - JSON: Mensaje de éxito con el token JWT y código de estado HTTP 200 si la autenticación es exitosa.
    - JSON: Mensaje de error y código de estado HTTP correspondiente en caso de falla.
"""
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return jsonify({"msg": "Email y contraseña son requeridos"}), 400

        user = Usuario.authenticate(email, password)

        if not user:
            return jsonify({"msg": "Credenciales incorrectas"}), 401

        access_token = user.generate_jwt()
        return jsonify(access_token=access_token, msg="Inicio de sesión exitoso"), 200

    except Exception as e:
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500



"""
    Endpoint para cerrar sesión de usuarios.

    Requiere un token JWT válido para acceder a la funcionalidad de cierre de sesión.
    Verifica si el usuario tiene permisos de 'empleado' antes de permitir el cierre de sesión.

    Returns:
    - JSON: Mensaje de éxito y código de estado HTTP 200 si el cierre de sesión es exitoso.
    - JSON: Mensaje de error y código de estado HTTP correspondiente en caso de falla.
"""
@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    try:
        user_id = get_jwt_identity()
        user = Usuario.get_by_id(user_id)

        if not user:
            return jsonify({"msg": "Usuario no encontrado"}), 404

        if user.rol != 'empleado':
            return jsonify({"msg": "Acceso denegado, no eres empleado."}), 403

        # Implementación del logout aquí (actualmente no implementado)

        return jsonify({"msg": "Cierre de sesión exitoso"}), 200

    except mysql.connector.Error as db_error:
        return jsonify({"msg": f"Error en la base de datos: {db_error}"}), 500
    except KeyError:
        return jsonify({"msg": "Token JWT inválido"}), 400
    except Exception as e:
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500
