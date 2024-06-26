from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

from app.database import init_app  
from app.auth.auth import auth_bp  
from app.views.setup import setup_bp  

# Cargar las variables de entorno desde el archivo .env
load_dotenv()


"""
    Función para crear y configurar la aplicación Flask.

    Returns:
        app (Flask): La aplicación Flask configurada.
"""
def create_app():
    app = Flask(__name__)
    
    # Configuración de modo DEBUG
    app.config['DEBUG'] = True

    # Configurar CORS para permitir todas las peticiones desde cualquier origen
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    # Configurar la clave secreta para JWT obteniéndola de las variables de entorno
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    jwt = JWTManager(app)

    # Inicializar la base de datos pasando la aplicación Flask como parámetro
    init_app(app)

    # Registrar los blueprints de las diferentes partes de la aplicación
    app.register_blueprint(auth_bp)    
    app.register_blueprint(setup_bp)   
    
    # Aquí se registrarían los blueprints adicionales para otras partes de la aplicación, por ejemplo:
    # app.register_blueprint(product_bp)
    # app.register_blueprint(order_bp)
    # app.register_blueprint(admin_bp)

    return app

if __name__ == '__main__':
    # Crear la aplicación Flask y ejecutarla en modo de desarrollo
    app = create_app()
    app.run()
