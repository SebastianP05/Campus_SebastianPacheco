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

import json

import json

def calificar_campers(id_camper, nombre_archivo_campers, nombre_archivo_notas):
    with open(nombre_archivo_campers, 'r') as file_campers:
        campers = json.load(file_campers)

    camper_encontrado = None
    for camper in campers:
        if camper['ID'] == id_camper:
            camper_encontrado = camper
            break

    if camper_encontrado is not None:
        
        if camper_encontrado['Estado'] == 'Aprobado':
            print("***************************")
            print("El camper ya está aprobado.")
            print("***************************")
            return

        nota_teoria = float(input("Ingrese la nota teórica del camper: "))
        nota_practica = float(input("Ingrese la nota práctica del camper: "))

        promedio = (nota_teoria + nota_practica) / 2

        if promedio >= 60:
            camper_encontrado['Estado'] = 'Aprobado'
            print("****************************************************")
            print("El camper ha sido aprobado con un promedio de", promedio)
            print("****************************************************")
        else:
            print("*************************************************************")
            print("El camper no ha alcanzado el promedio necesario para aprobar.")
            print("*************************************************************")

        with open(nombre_archivo_campers, 'w') as file_campers:
            json.dump(campers, file_campers)

        with open(nombre_archivo_notas, 'a') as file_notas:
            json.dump({'ID': id_camper, 'NotaTeoria': nota_teoria, 'NotaPractica': nota_practica}, file_notas)
            file_notas.write('\n')

    else:
        print(f"No se encontró un camper con el ID {id_camper} en el archivo de campers.")



