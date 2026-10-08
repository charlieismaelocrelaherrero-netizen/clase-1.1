carreras: tuple[str, ...] = (
    "Ingeniería de Software",
    "Contabilidad",
    "Derecho"
)

personas: list[tuple[str, str, int, int]] = [
    # nombre, apellido, edad, carrera
]

estudiantes: list[dict[str, str | int]] = [
    # Lista de diccionario con nombre, apellido, edad, carrera
]

for _ in range(5):
    # Solicita los datos aquí
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))

    print("Carreras disponibles:")
    print("0 - Ingeniería de Software")
    print("1 - Contabilidad")
    print("2 - Derecho")

    carrera = int(input("Ingrese el número de su carrera: "))

    # Crear la tupla y agregarla a personas
    persona = (nombre, apellido, edad, carrera)
    personas.append(persona)

    print("")

# Recorrer personas y crear los diccionarios
for persona in personas:
    nombre = persona[0]
    apellido = persona[1]
    edad = persona[2]
    carrera = carreras[persona[3]]

    estudiante = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "carrera": carrera
    }

    estudiantes.append(estudiante)

# Mostrar la información de los estudiantes
for estudiante in estudiantes:
    print(
        f"{estudiante['nombre']} {estudiante['apellido']} "
        f"tiene {estudiante['edad']} años y estudia "
        f"{estudiante['carrera']}"
    )