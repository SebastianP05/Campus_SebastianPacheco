
import json

def registrar_camper(campers, nombre_archivo):
    id = input("Ingrese el número de identificación del camper: ")
    nombre = input("Ingrese el nombre del camper: ")
    apellido = input("Ingrese el apellido del camper: ")
    direccion = input("Ingresa la dirección del camper: ")
    acudiente = input("Ingrese el nombre del acudiente: ")
    telefono = input("Ingrese el número de teléfono del camper: ")

    camper = {
        'ID': id,
        'Nombre': nombre,
        'Apellido': apellido,
        'Direccion': direccion,
        'Acudiente': acudiente,
        'Telefono': telefono,
        'Estado': 'En proceso de ingreso',
    }

    campers.append(camper)

    print("Camper registrado exitosamente.")
    print("ID:", camper['ID'])
    print("Nombre:", camper['Nombre'])
    print("Apellido:", camper['Apellido'])
    print("Dirección:", camper['Direccion'])
    print("Acudiente:", camper['Acudiente'])
    print("Teléfono:", camper['Telefono'])
    print("Estado:", camper['Estado'])

    camper = gestionar_estado_camper(camper)

    guardar_en_archivo(campers, nombre_archivo)  
    return campers

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

def guardar_en_archivo(campers, nombre_archivo):
    with open(nombre_archivo, 'w') as file:
        json.dump(campers, file)

nombre_archivo = 'campers.json'
campers = []
campers = registrar_camper(campers, nombre_archivo)
print(campers)
