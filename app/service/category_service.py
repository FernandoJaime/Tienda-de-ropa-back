from ..models.categoria import Categoria

def create_category(data):
    categoria = Categoria(
        nom_categoria=data.get('nom_categoria'),
        cod_categoria=data.get('cod_categoria')
    )
    categoria.save()
    return categoria

def get_all_categories():
    return Categoria.get_all_categories()

def get_category_by_id():
    return Categoria.get_cat_by_id()
