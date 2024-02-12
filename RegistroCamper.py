import json

def gestionar_estado_camper(camper):

    print("Estados disponibles:")
    print("1. En proceso de ingreso")
    print("2. Inscrito")
    print("3. Aprobado")
    print("4. Cursando")
    print("5. Graduado")
    print("6. Expulsado")
    print("7. Retirado")

    opcion = input("Ingrese el número correspondiente al nuevo estado: ")

    estados = {
        '1': 'En proceso de ingreso',
        '2': 'Inscrito',
        '3': 'Aprobado',
        '4': 'Cursando',
        '5': 'Graduado',
        '6': 'Expulsado',
        '7': 'Retirado',
    }

    nuevo_estado = estados.get(opcion, 'Estado no válido')

    if nuevo_estado != 'Estado no válido':
        camper['estado'] = nuevo_estado
        print("Estado actualizado exitosamente.")
    else:
        print("Opción no válida. El estado no ha sido actualizado.")

    return camper

def registrar_camper(campers):
    id = input("Ingrese el número de identificación del camper: ")
    nombre = input("Ingrese el nombre del camper: ")
    apellido = input("Ingrese el apellido del camper: ")
    direccion = input("Ingresa la direccion del camper: ")
    acudiente = input("Ingrese el nombre del acudiente: ")
    telefono = input("Ingrese el numero de teléfono del camper: ")

    camper = {
        'ID': id,
        'nombre': nombre,
        'apellido': apellido,
        'direccion': direccion,
        'acudiente': acudiente,
        'telefono': telefono,
        'estado': 'En proceso de ingreso',
    }

    campers.append(camper)

    print("Camper registrado exitosamente.")
    print("ID:", camper['ID'])
    print("Nombre:", camper['nombre'])
    print("Apellido:", camper['apellido'])
    print("Dirección:", camper['direccion'])
    print("Acudiente:", camper['acudiente'])
    print("Teléfono:", camper['telefono'])
    print("Estado:", camper['estado'])

    camper = gestionar_estado_camper(camper)

    guardar_en_archivo(campers, 'campers.json')  
    return campers

def guardar_en_archivo(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def cargar_desde_archivo(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

nombre_archivo = 'campers.json'
