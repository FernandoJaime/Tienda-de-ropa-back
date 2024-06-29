from ..models.Producto import Producto

def create_product(data):
    cod_categoria = data.get('cod_categoria')
    tipo_producto = data.get('tipo_producto')
    nom_producto = data.get('nom_producto')
    precio_unitario = data.get('precio_unitario')
    img_producto = data.get('img_producto')
    stock_pro = data.get('stock_pro')
    descripcion_pro = data.get('descripcion_pro')

    nuevo_producto = Producto(
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
