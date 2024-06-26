import mysql.connector
from flask import g
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos obtenida desde las variables de entorno
DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 3306), 
}



"""
    Obtiene una conexión a la base de datos.

    Retorna:
    - Conexión a la base de datos usando las configuraciones definidas en DATABASE_CONFIG.
"""
def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    return g.db


"""
    Cierra la conexión a la base de datos.

    Args:
    - e: Parámetro opcional, no utilizado en esta función.
"""
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


"""
    Inicializa la aplicación para el manejo de la base de datos.

    Args:
    - app: Instancia de la aplicación Flask.
"""
def init_app(app):
    app.teardown_appcontext(close_db)
