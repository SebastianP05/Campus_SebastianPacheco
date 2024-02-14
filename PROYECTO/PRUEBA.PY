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

def menu_camper():
    print("********************")
    print("Bienvenido Camper.")
    print("********************")
    while True:
        accion = int(input("¿Qué deseas hacer?\n" +
                           "\n1. Registrarte.\n" +
                           "2. Actualizar estado.\n" +
                           "3. Reservar plaza en un parque.\n" +
                           "4. Cancelar reserva.\n" +
                           "5. Salir al menú principal.\n"))
        if accion == 1:

            print("*********************************")
            campers=0
            Camper.registrar_camper(campers, nombre_archivo='campers.json')
            print("************************************")
            volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
            if volver_al_menu != 'si':
                break
            
        elif accion == 2:
            print("******************************")
            id_camper = input("Ingrese el ID del camper que desea gestionar: ")
            print("**********************************************************")
            Camper.gestionar_y_guardar_estado_camper(id_camper, nombre_archivo='campers.json')
            print("******************************")
            volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
            if volver_al_menu != 'si':
                break
        elif accion == 3:
            # Lógica para la opción 3
            pass
        elif accion == 4:
            # Lógica para la opción 4
            pass
        elif accion == 5:
            main_menu()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Importa el módulo Camper después de definir todas las funciones
import Camper

# Llama a la función principal
main_menu()
