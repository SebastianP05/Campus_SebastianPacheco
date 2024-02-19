import json

def agregar_rutas_y_asignar_campers():
    # Agregar nuevas rutas
    with open('rutas.json', 'r') as file:
        rutas_existentes = json.load(file)

    nueva_ruta = {
        "nombre": "Nueva Ruta",
        "cursos": [
            "Fundamentos de programación",
            "Programación Web",
            "Programación formal",
            "Bases de datos",
            "Backend"
        ],
        "sgdb_principal": "Mysql",
        "sgdb_alternativo": "Postgresql",
        "capacidad_maxima": 33,
        "campers": []  # Agrega una lista para almacenar los campers asignados a esta ruta
    }

    rutas_existentes.append(nueva_ruta)

    with open('rutas.json', 'w') as file:
        json.dump(rutas_existentes, file, indent=2)

    # Asignar campers a las rutas
    with open('campers.json', 'r') as file:
        campers = json.load(file)

    camper_id = input("Ingrese el ID del camper: ")

    camper_encontrado = None
    for camper in campers:
        if camper['id'] == camper_id:
            camper_encontrado = camper
            break

    if not camper_encontrado:
        print(f"No se encontró un camper con el ID {camper_id}")
        return

    ruta_asignada = None
    for ruta in rutas_existentes:
        if len(ruta['campers']) < ruta['capacidad_maxima']:
            ruta_asignada = ruta['nombre']
            ruta['campers'].append(camper_encontrado)
            break

    if ruta_asignada:
        print(f"El camper {camper_encontrado['nombre']} ha sido asignado a la ruta {ruta_asignada}")
    else:
        print(f"No hay rutas disponibles para el camper {camper_encontrado['nombre']}")

# Ejemplo de uso
agregar_rutas_y_asignar_campers()


def dirigir_rutas(rutas, horarios):
    for ruta in rutas:
        print(f"\nRuta: {ruta['nombre']}")
        print("Cursos:")
        for curso in ruta['cursos']:
            print(f"- {curso}")

        print(f"SGDB Principal: {ruta['sgdb_principal']}")
        print(f"SGDB Alternativo: {ruta['sgdb_alternativo']}")
        print(f"Capacidad Máxima: {ruta['capacidad_maxima']}")
        print("Campers asignados:")
        for camper in ruta['campers']:
            print(f"- {camper}")

        print(f"\nHorarios:")
        for horario in horarios[ruta['nombre']]:
            print(f"- {horario}")

horarios_rutas = {
    "Nueva Ruta": ["Lunes 10:00 AM - 12:00 PM", "Miércoles 2:00 PM - 4:00 PM"],
    
}

dirigir_rutas(horarios_rutas)

import json

def evaluar_campers(campers):
    for camper in campers:
        
        nota_teorica = int(input("Por favor ingresa la nota teorica."))
        nota_practica = int(input("Por favor ingresa la nota practica."))

        promedio_ponderado = (nota_teorica * 0.3) + (nota_practica * 0.6)

        camper['nota_teorica'] = nota_teorica
        camper['nota_practica'] = nota_practica
        camper['promedio_ponderado'] = promedio_ponderado

        
        if promedio_ponderado >= 60:
            camper['estado_modulo'] = 'Aprobado'
        else:
            camper['estado_modulo'] = 'Reprobado'

    with open('campers.json', 'w') as file:
        json.dump(campers, file, indent=2)

with open('campers.json', 'r') as file:
    campers_list = json.load(file)

evaluar_campers(campers_list)


