# Funciones que verifican que los datos ingresados por el usuario sean correctos.
# Si algo falla, lanzan un ValueError con un mensaje claro.


# Verifica que el nombre no esté vacío y solo tenga letras y espacios.
def validar_nombre(nombre: str) -> bool:
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if not all(c.isalpha() or c.isspace() for c in nombre.strip()):
        raise ValueError("El nombre solo puede contener letras y espacios.")
    return True


# Verifica que la edad sea un número entre 1 y 120. Devuelve el número ya convertido.
def validar_edad(edad: str) -> int:
    try:
        edad_int = int(edad)
    except ValueError:
        raise ValueError("La edad debe ser un número entero.")
    if not (1 <= edad_int <= 120):
        raise ValueError("La edad debe estar entre 1 y 120 años.")
    return edad_int


# Verifica que el email tenga un formato básico válido (contiene @ y un punto después).
def validar_email(email: str) -> bool:
    if not email or "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("El correo electrónico no tiene un formato válido.")
    return True
