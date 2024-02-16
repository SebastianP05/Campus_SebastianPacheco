from Camper import registrar_camper

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

#def menu_trainer():#

def menu_coordinador():
    print("***********************")
    print("Bienvenido Coordinador.")
    print("***********************")
    while True:
        accion = int(input("¿Qué deseas hacer?\n" +
                           "\n1. Cambiar estado del camper.\n" +
                           "2. Salir al menú principal.\n"))
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
            main_menu()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

from Coordinador import gestionar_y_guardar_estado_camper