import json

def gestionar_y_guardar_estado_camper(id_camper, nombre_archivo):
    
    nombre_archivo='campers.json'

    with open(nombre_archivo, 'r') as file:
        campers = json.load(file)

    camper_encontrado = None
    for camper in campers:
        if camper['ID'] == id_camper:
            camper_encontrado = camper
            break

    if camper_encontrado is not None:
        print("***************************")
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
            camper_encontrado['Estado'] = nuevo_estado
            print("Estado actualizado exitosamente.")
        else:
            print("Opción no válida. El estado no ha sido actualizado.")
    else:
        print(f"No se encontró un camper con el ID {id_camper}.")

    with open(nombre_archivo, 'w') as file:
        json.dump(campers, file)


