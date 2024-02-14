import FuCampers 

def menu_camper():
    print("********************")
    print("Bienvenido Camper.")
    print("********************")
    while True:
        accion = int(input("¿Qué deseas hacer?\n" +
                           "1. Registrarte.\n" +
                           "2. Actualizar estado.\n" +
                           "3. Reservar plaza en un parque.\n" +
                           "4. Cancelar reserva.\n" +
                           "5. Salir al menú principal.\n"))
        if accion == 1:
            print("*********************************")
            nombre_archivo = 'campers.json'
            campers = []
            FuCampers.registrar_camper(campers, nombre_archivo)
            print("************************************")

            volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
            if volver_al_menu != 'si':
                break  # Salir del bucle si la respuesta no es 'Sí'
        elif accion == 2:
            FuCampers.gestionar_y_guardar_estado_camper
            pass
        elif accion == 3:
            # Lógica para la opción 3
            pass
        elif accion == 4:
            # Lógica para la opción 4
            pass
        elif accion == 5:
            # Lógica para la opción 5
            break  # Salir del bucle si se elige la opción 5
        else:
            print("Opción no válida. Inténtalo de nuevo.")


def menu_trainer():
    # Definir el menú del Trainer aquí
    pass

def menu_coordinador():
    # Definir el menú del Coordinador aquí
    pass

def reservacion_plazas():
    # Definir la lógica para la reservación de plazas aquí
    pass

def cancelar_reserva():
    # Definir la lógica para cancelar reserva aquí
    pass

def main_menu():
    print("********************************************")
    print("Bienvenido a CAMPUSLANDS.")
    print("**********************************************")
    print("Por el momento solo tenemos 3 roles de usuario")
    print("""**********************************************      
        1. Camper.
        2. Trainer.
        3. Coordinador.""")
    print("********************************************")
    
    rol = int(input("Por favor elige tu rol: "))

    if rol == 1:
        menu_camper()
    elif rol == 2:
        menu_trainer()
    elif rol == 3:
        menu_coordinador()
    else:
        print('********************************')
        print('Error, elige una opción válida.')
        print('********************************')
        return

