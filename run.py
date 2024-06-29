# Importa la función create_app desde el módulo app
from app import create_app

# Punto de entrada principal del programa
if __name__ == '__main__':
    # Crea una instancia de la aplicación Flask usando la función create_app
    app = create_app()

    # Ejecuta la aplicación en el servidor web integrado de Flask
    app.run()
