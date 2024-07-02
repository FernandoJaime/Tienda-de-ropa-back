from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..service.product_service import create_product, get_all_products, delete_product_by_id, update_product, get_product_by_id


# Definición del blueprint para gestionar rutas relacionadas con productos
product_bp = Blueprint('productos', __name__, url_prefix='/productos')

# Endpoint para la creación de un nuevo producto
@product_bp.route('/registro', methods=['POST'])
@jwt_required()  # Protegido por autenticación JWT
def create_product_endpoint():
    data = request.json

    # Validación de campos obligatorios en la solicitud
    if not all([data.get('nom_producto'), data.get('cod_categoria'), data.get('tipo_categoria'), 
                data.get('tipo_producto'), data.get('precio_unitario'), data.get('img_producto'), 
                data.get('stock_pro'), data.get('descripcion_pro')]):
        return jsonify({"msg": "Faltan datos"}), 400

    try:
        # Intentar crear un nuevo producto usando el servicio correspondiente
        nuevo_producto = create_product(data)
        return jsonify(nuevo_producto.serialize()), 201  # Devolver el nuevo producto creado
    except Exception as e:
        # Capturar cualquier excepción y devolver un mensaje de error adecuado
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500

# Endpoint para obtener todos los productos
@product_bp.route('/listar', methods=['GET'])
@jwt_required()  # Protegido por autenticación JWT
def get_all_products_endpoint():
    try:
        # Intentar obtener todos los productos usando el servicio correspondiente
        productos = get_all_products()
        return jsonify(productos), 200  # Devolver la lista de productos
    except Exception as e:
        # Capturar cualquier excepción y devolver un mensaje de error adecuado
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500

# Endpoint para eliminar un producto por su ID
@product_bp.route('/eliminar/<int:producto_id>', methods=['DELETE'])
@jwt_required()  # Protegido por autenticación JWT
def delete_product_endpoint(producto_id):
    try:
        # Intentar eliminar el producto usando el servicio correspondiente
        delete_result = delete_product_by_id(producto_id)
        
        if delete_result:
            return jsonify({"msg": "Producto eliminado correctamente"}), 200
        else:
            return jsonify({"msg": "Producto no encontrado"}), 404
    except Exception as e:
        # Capturar cualquier excepción y devolver un mensaje de error adecuado
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500
    

# Endpoint para actualizar un producto por su ID
@product_bp.route('/editar/<int:cod_producto>', methods=['PUT'])
@jwt_required()
def update_product_endpoint(cod_producto):

    try:
        data = request.json
        updated_product = update_product(cod_producto, data)
        if updated_product:
            return jsonify(updated_product.serialize()), 200
        else:
            return jsonify({"msg": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500


# Endpoint para obtener un producto por su ID
@product_bp.route('/<int:cod_producto>', methods=['GET'])
@jwt_required()  # Protegido por autenticación JWT
def get_product_by_id_endpoint(cod_producto):
    
    try:
        product = get_product_by_id(cod_producto)
        if product:
            return jsonify(product.serialize()), 200
        else:
            return jsonify({"msg": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"msg": f"Error en el servidor: {str(e)}"}), 500
    

