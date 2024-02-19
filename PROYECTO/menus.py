import json

def main_menu():

    print("********************************************")
    print("Bienvenido a CAMPUSLANDS.")
    print("**********************************************")
    print("Por el momento solo tenemos 3 roles de usuario")
    print("Presiona 4 si deseas salir.")
    print("""**********************************************      
        1. Camper.
        2. Trainer.
        3. Coordinador.
        4. Salir   
          """)
    print("********************************************")
    
    rol = int(input("Por favor elige tu rol: "))

    if rol == 1:
        menu_camper()
    elif rol == 2:
        menu_trainer()
    elif rol == 3:
        menu_coordinador()
    elif rol == 4:
        salir = input("¿Estás seguro que deseas salir? (Sí/No): ").lower()
        if salir != 'no':
            main_menu()
    else:
        print('********************************')
        print('Error, elige una opción válida.')
        print('********************************')
        return

from Camper import registrar_camper

def menu_camper():
    print("********************")
    print("Bienvenido Camper.")
    print("********************")
    while True:
        accion = int(input("¿Qué deseas hacer?\n" +
                           "\n1. Registrarte.\n" +
                           "2. Salir al menú principal.\n"))
        if accion == 1:

            print("*********************************")
            campers_list = []
            registrar_camper(campers_list, "campers.json")
            print("************************************")
            volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
            if volver_al_menu != 'si':
                break
        elif accion == 2:
            main_menu()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_trainer():

    print("********************")
    print("Bienvenido Trainer.")
    print("********************")
    while True:

        accion = int(input("¿Qué deseas hacer?\n" +
                           "\n1. Agregar rutas y asignar camper.\n" +
                           "2. Evaluar campers.\n"))
        if accion == 1:
              
                print("********************************")
                print("Haz añadido estas rutas nuevas: " +
                      "********************************"
                      "- Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)" +
                      "- Programación Web (HTML, CSS y Bootstrap)." +
                      "- Programación formal (Java, JavaScript, C#)." + 
                      "- Bases de datos (Mysql, MongoDb y Postgresql)." +
                      "- Backend (NetCore, Spring Boot, NodeJS y Express)."
                      )
                print("********************************")
                agregar_rutas_y_asignar_campers()
                volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
                if volver_al_menu != 'si':
                    break
        elif accion == 2:
                
                evaluar_campers(campers_list)
                
with open('campers.json', 'r') as file:
                campers_list = json.load(file)

from Trainer import  agregar_rutas_y_asignar_campers
from Trainer import evaluar_campers

def menu_coordinador():

    print("***********************")
    print("Bienvenido Coordinador.")
    print("***********************")
    while True:
        accion = int(input("¿Qué deseas hacer?\n" +
                           "\n1. Cambiar estado del camper.\n" +
                           "2. Calificacion camper.\n"))
        if accion == 1:
            print("******************************")
            id_camper = input("Ingrese el ID del camper que desea gestionar: ")
            print("**********************************************************")
            nombre_archivo='campers.json'
            gestionar_y_guardar_estado_camper(id_camper, nombre_archivo)
            print("******************************")
            volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
            if volver_al_menu != 'si':
                break    
        elif accion == 2:
            id_camper_a_calificar = input("Ingrese el ID del camper a calificar: ")
            nombre_archivo_campers = 'campers.json'
            nombre_archivo_notas = 'notas.json'
            calificar_campers(id_camper_a_calificar, nombre_archivo_campers, nombre_archivo_notas)
            volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
            if volver_al_menu != 'si':
                break    
        

            
from Coordinador import gestionar_y_guardar_estado_camper
from Coordinador import calificar_campers