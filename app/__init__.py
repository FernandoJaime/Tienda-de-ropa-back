# Importación de módulos y clases necesarias desde Flask y otras bibliotecas
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Importación de funciones y blueprints desde el directorio local 'app'
from .database import init_app
from .routes.authRoutes import auth_bp
from .routes.usuarioRoutes import setup_bp
from .routes.productosRoutes import product_bp
from .routes.categoriaRoute import category_bp

# Función para crear y configurar una aplicación Flask
def create_app():
    #Crea una instancia de la aplicación Flask con configuraciones y extensiones predefinidas. 

    # Crea una instancia de la aplicación 
    app = Flask(__name__)

    # Carga las variables de entorno desde el archivo .env en las variables de configuración de la aplicación
    load_dotenv()

    # Configuración de modo debug para la aplicación Flask
    app.config['DEBUG'] = True

    # Configuración de la clave secreta JWT obtenida desde las variables de entorno
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Configuración CORS para permitir solicitudes desde cualquier origen
    CORS(app)

    # Configuración del administrador JWT para la gestión de tokens JWT
    JWTManager(app)

    # Inicialización de la base de datos de la aplicación
    init_app(app)

    # Registro de blueprints para manejar rutas de autenticación y de usuario y productos
    app.register_blueprint(auth_bp)     
    app.register_blueprint(setup_bp)  
    app.register_blueprint(product_bp)   
    app.register_blueprint(category_bp)

    # Devuelve la instancia de la aplicación Flask configurada
    return app
