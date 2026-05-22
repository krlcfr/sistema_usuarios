# Maneja todas las operaciones sobre usuarios: registrar, listar y buscar.
# Los usuarios se guardan en memoria mientras el programa está corriendo.

from app.usuarios.validaciones import validar_nombre, validar_edad, validar_email

_usuarios: list[dict] = []


# Valida los datos y agrega un nuevo usuario a la lista. Rechaza correos duplicados.
def registrar_usuario(nombre: str, edad: str, email: str) -> dict:
    validar_nombre(nombre)
    edad_valida = validar_edad(edad)
    validar_email(email)

    if buscar_usuario(email):
        raise ValueError(f"Ya existe un usuario con el email '{email}'.")

    usuario = {
        "id"    : len(_usuarios) + 1,
        "nombre": nombre.strip().title(),
        "edad"  : edad_valida,
        "email" : email.strip().lower(),
    }
    _usuarios.append(usuario)
    return usuario


# Devuelve todos los usuarios registrados.
def listar_usuarios() -> list[dict]:
    return list(_usuarios)


# Busca un usuario por su email exacto. Devuelve el usuario o None si no existe.
def buscar_usuario(email: str) -> dict | None:
    email_lower = email.strip().lower()
    for usuario in _usuarios:
        if usuario["email"] == email_lower:
            return usuario
    return None


# Busca usuarios cuyo nombre contenga el texto ingresado (no importa mayúsculas).
def buscar_por_nombre(nombre: str) -> list[dict]:
    termino = nombre.strip().lower()
    return [u for u in _usuarios if termino in u["nombre"].lower()]
