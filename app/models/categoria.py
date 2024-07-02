from ..database import get_db

class Categoria:

    def __init__(self, nom_categoria, cod_categoria =  None):
        self.cod_categoria = cod_categoria
        self.nom_categoria = nom_categoria

    def serialize(self):
        return {
            'cod_categoria': self.cod_categoria,
            'nom_categoria': self.nom_categoria
        }

    @staticmethod
    def get_all_categories():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM Categorias"
        cursor.execute(query)
        rows = cursor.fetchall()
        categories = [Categoria(cod_categoria=row['cod_categoria'], nom_categoria=row['nom_categoria']).serialize() for row in rows]
        cursor.close()
        return categories
    
    @staticmethod
    def get_cat_by_id(cod_categoria):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Categorias WHERE cod_categoria = %s", (cod_categoria,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Categoria(cod_categoria=row[0], nom_categoria=row[1])
        else:
            return None
    