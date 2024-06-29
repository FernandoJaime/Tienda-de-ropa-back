from ..database import get_db

class Producto:

    def __init__(self, cod_categoria, nom_producto, tipo_producto, precio_unitario, img_producto, stock_pro, descripcion_pro, cod_producto = None):
        self.cod_producto = cod_producto
        self.cod_categoria = cod_categoria
        self.tipo_producto = tipo_producto
        self.nom_producto = nom_producto
        self.precio_unitario = precio_unitario
        self.img_producto = img_producto
        self.stock_pro = stock_pro
        self.descripcion_pro = descripcion_pro

    def serialize(self):
        return {
            'cod_producto': self.cod_producto,
            'cod_categoria': self.cod_categoria,
            'tipo_producto': self.tipo_producto,
            'nom_producto': self.nom_producto,
            'precio_unitario': self.precio_unitario,
            'img_producto': self.img_producto,
            'stock_pro': self.stock_pro,
            'descripcion_pro': self.descripcion_pro
        }

    @staticmethod
    def get_all_products():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM productos"
        cursor.execute(query)
        rows = cursor.fetchall()
        products = [Producto(cod_producto=row['cod_producto'], cod_categoria=row['cod_categoria'], tipo_producto=row['tipo_producto'], nom_producto=row['nom_producto'], precio_unitario=row['precio_unitario'], img_producto=row['img_producto'], stock_pro=row['stock_pro'], descripcion_pro=row['descripcion_pro']).serialize() for row in rows]
        cursor.close()
        return products

    @staticmethod
    def get_product_by_id(cod_producto):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE cod_producto = %s", (cod_producto,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Producto(cod_producto=row[0], cod_categoria=row[1], tipo_producto=row[2], nom_producto=row[3], precio_unitario=row[4], img_producto=row[5], stock_pro=row[6], descripcion_pro=row[7])
        else:
            return None
        
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.cod_producto:
            cursor.execute("""
                UPDATE productos SET cod_categoria = %s, tipo_producto = %s, nom_producto = %s, precio_unitario = %s, img_producto = %s, stock_pro = %s, descripcion_pro = %s 
                WHERE cod_producto = %s
            """, (self.cod_categoria, self.tipo_producto, self.nom_producto, self.precio_unitario, self.img_producto, self.stock_pro, self.descripcion_pro, self.cod_producto))
        else:
            cursor.execute("""
                INSERT INTO productos(cod_categoria, tipo_producto, nom_producto, precio_unitario, img_producto, stock_pro, descripcion_pro) 
                VALUES(%s, %s, %s, %s, %s, %s, %s)
            """, (self.cod_categoria, self.tipo_producto, self.nom_producto, self.precio_unitario, self.img_producto, self.stock_pro, self.descripcion_pro))
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE cod_producto = %s", (self.cod_producto,))
        db.commit()
        cursor.close()