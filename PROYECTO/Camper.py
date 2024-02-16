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

    nombre_archivo="campers.json"

    with open(nombre_archivo, 'w') as file:
        json.dump(campers, file)

    return campers