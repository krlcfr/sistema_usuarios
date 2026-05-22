# Lee las variables del archivo .env y las expone como constantes para toda la app.

import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME    = os.getenv("APP_NAME", "Sistema Usuarios")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
ADMIN_USER  = os.getenv("ADMIN_USER", "admin")


# Muestra en consola los valores cargados desde .env.
def mostrar_config():
    print(f"  Aplicación : {APP_NAME}")
    print(f"  Versión    : {APP_VERSION}")
    print(f"  Admin      : {ADMIN_USER}")
