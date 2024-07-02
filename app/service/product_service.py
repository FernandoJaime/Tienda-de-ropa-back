from ..models.Producto import Producto
from ..database import get_db


def create_product(data):
    cod_producto = data.get('cod_producto')
    cod_categoria = data.get('cod_categoria')
    tipo_producto = data.get('tipo_producto').capitalize()
    nom_producto = data.get('nom_producto').capitalize()
    precio_unitario = data.get('precio_unitario')
    img_producto = data.get('img_producto')
    stock_pro = data.get('stock_pro')
    descripcion_pro = data.get('descripcion_pro').capitalize()

    nuevo_producto = Producto(
        cod_producto=cod_producto,
        cod_categoria=cod_categoria,
        tipo_producto=tipo_producto,
        nom_producto=nom_producto,
        precio_unitario=precio_unitario,
        img_producto=img_producto,
        stock_pro=stock_pro,
        descripcion_pro=descripcion_pro
    )

    nuevo_producto.save()
    return nuevo_producto

def get_all_products():
    return Producto.get_all_products()

def get_product_by_id(cod_producto):
    db = get_db()
    cursor = db.cursor(dictionary=True)  # Para obtener resultados como diccionarios
    cursor.execute("SELECT * FROM Productos WHERE cod_producto = %s", (cod_producto,))
    row = cursor.fetchone()
    cursor.close()
    if row:
        return Producto(
            cod_producto=row['cod_producto'],
            cod_categoria=row['cod_categoria'],
            tipo_producto=row['tipo_producto'],
            nom_producto=row['nom_producto'],
            precio_unitario=row['precio_unitario'],
            img_producto=row['img_producto'],
            stock_pro=row['stock_pro'],
            descripcion_pro=row['descripcion_pro']
        )
    else:
        return None


def delete_product_by_id(cod_producto):
    product = Producto.get_product_by_id(cod_producto)
    if product:
        product.delete()
        return True
    else:
        return False

def update_product(cod_producto, data):
    product = Producto.get_product_by_id(cod_producto)
    if product:
        product.tipo_producto = data.get('tipo_producto', product.tipo_producto).capitalize()
        product.nom_producto = data.get('nom_producto', product.nom_producto).capitalize()
        product.precio_unitario = data.get('precio_unitario', product.precio_unitario)
        product.img_producto = data.get('img_producto', product.img_producto)
        product.stock_pro = data.get('stock_pro', product.stock_pro)
        product.descripcion_pro = data.get('descripcion_pro', product.descripcion_pro).capitalize()

        product.save()  
        return product
    else:
        return None