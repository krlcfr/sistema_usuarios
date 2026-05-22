# Punto de entrada del programa. Muestra el menú y conecta las acciones del usuario
# con las funciones de cada módulo.

from app.config.settings import APP_NAME, APP_VERSION, ADMIN_USER
from app.usuarios.gestor import (
    registrar_usuario,
    listar_usuarios,
    buscar_usuario,
    buscar_por_nombre,
)


# Encabezado que se muestra al iniciar el programa.
def imprimir_encabezado():
    print("\n" + "=" * 45)
    print(f"  {APP_NAME}  v{APP_VERSION}")
    print(f"  Admin: {ADMIN_USER}")
    print("=" * 45)


# Opciones del menú principal.
def imprimir_menu():
    print("\n  [1] Registrar usuario")
    print("  [2] Listar usuarios")
    print("  [3] Buscar por email")
    print("  [4] Buscar por nombre")
    print("  [0] Salir")
    print("-" * 45)


# Pide los datos al usuario y llama a registrar_usuario. Muestra error si algo falla.
def flujo_registrar():
    print("\n--- Registrar nuevo usuario ---")
    try:
        nombre  = input("  Nombre : ").strip()
        edad    = input("  Edad   : ").strip()
        email   = input("  Email  : ").strip()
        usuario = registrar_usuario(nombre, edad, email)
        print(f"\n  ✔ Usuario registrado: {usuario['nombre']} (ID {usuario['id']})")
    except ValueError as e:
        print(f"\n  ✘ Error: {e}")


# Muestra todos los usuarios registrados en la sesión actual.
def flujo_listar():
    print("\n--- Lista de usuarios ---")
    usuarios = listar_usuarios()
    if not usuarios:
        print("  (no hay usuarios registrados)")
        return
    for u in usuarios:
        print(f"  [{u['id']}] {u['nombre']} | {u['edad']} años | {u['email']}")


# Busca un usuario por email exacto y muestra sus datos.
def flujo_buscar_email():
    print("\n--- Buscar por email ---")
    email   = input("  Email : ").strip()
    usuario = buscar_usuario(email)
    if usuario:
        print(f"\n  Encontrado: {usuario['nombre']} | {usuario['edad']} años | {usuario['email']}")
    else:
        print(f"\n  No se encontró ningún usuario con el email '{email}'.")


# Busca usuarios cuyo nombre contenga el texto ingresado.
def flujo_buscar_nombre():
    print("\n--- Buscar por nombre ---")
    nombre     = input("  Nombre (parcial) : ").strip()
    resultados = buscar_por_nombre(nombre)
    if resultados:
        for u in resultados:
            print(f"  [{u['id']}] {u['nombre']} | {u['edad']} años | {u['email']}")
    else:
        print(f"  No se encontraron usuarios con '{nombre}'.")


# Bucle principal: muestra el menú y ejecuta la opción elegida.
def main():
    imprimir_encabezado()
    opciones = {
        "1": flujo_registrar,
        "2": flujo_listar,
        "3": flujo_buscar_email,
        "4": flujo_buscar_nombre,
    }
    while True:
        imprimir_menu()
        opcion = input("  Opción: ").strip()
        if opcion == "0":
            print("\n  Hasta luego.\n")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("  Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
