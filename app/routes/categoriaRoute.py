from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..service.category_service import create_category, get_all_categories, get_category_by_id

# Definición del blueprint para gestionar rutas relacionadas con categorías
category_bp = Blueprint('categorias', __name__, url_prefix='/categorias')

# Endpoint para la creación de una nueva categoría
@category_bp.route('/registro', methods=['POST'])
@jwt_required()  # Protegido por autenticación JWT
def create_category_endpoint():
    data = request.json

    # Validación de datos
    if not all([data.get('nom_categoria'), data.get('cod_categoria')]):
        return jsonify({"msg": "Faltan datos"}), 400

    try:
        # Intentar crear una nueva categoría usando el servicio correspondiente
        nueva_categoria = create_category(data)
        return jsonify(nueva_categoria.serialize()), 201  # Devolver la nueva categoría creada
    except Exception as e:
        # Capturar cualquier excepción y devolver un mensaje de error adecuado
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500

# Endpoint para obtener todas las categorías
@category_bp.route('/listar', methods=['GET'])
@jwt_required()  # Protegido por autenticación JWT
def get_all_categories_endpoint():
    try:
        # Intentar obtener todas las categorías usando el servicio correspondiente
        categorias = get_all_categories()
        return jsonify(categorias), 200  # Devolver la lista de categorías
    except Exception as e:
        # Capturar cualquier excepción y devolver un mensaje de error adecuado
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500

# Endpoint para obtener una categoría por ID
@category_bp.route('/<int:cod_categoria>', methods=['GET'])
@jwt_required()  # Protegido por autenticación JWT
def get_category_by_id_endpoint(cod_categoria):
    try:
        categoria = get_category_by_id(cod_categoria)
        if categoria:
            return jsonify(categoria.serialize()), 200  # Devolver la categoría encontrada
        else:
            return jsonify({"msg": "Categoría no encontrada"}), 404
    except Exception as e:
        # Capturar cualquier excepción y devolver un mensaje de error adecuado
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500