from ..models.Producto import Producto

def create_product(data):
    cod_producto = data.get('cod_producto')
    cod_categoria = data.get('cod_categoria')
    tipo_producto = data.get('tipo_producto')
    nom_producto = data.get('nom_producto')
    precio_unitario = data.get('precio_unitario')
    img_producto = data.get('img_producto')
    stock_pro = data.get('stock_pro')
    descripcion_pro = data.get('descripcion_pro')

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
    return Producto.get_product_by_id(cod_producto)

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
        # Actualizar los atributos del producto con los datos recibidos
        product.cod_categoria = data.get('cod_categoria', product.cod_categoria)
        product.tipo_producto = data.get('tipo_producto', product.tipo_producto)
        product.nom_producto = data.get('nom_producto', product.nom_producto)
        product.precio_unitario = data.get('precio_unitario', product.precio_unitario)
        product.img_producto = data.get('img_producto', product.img_producto)
        product.stock_pro = data.get('stock_pro', product.stock_pro)
        product.descripcion_pro = data.get('descripcion_pro', product.descripcion_pro)

        # Guardar los cambios en la base de datos
        product.update()

        return product
    else:
        return None
    
    