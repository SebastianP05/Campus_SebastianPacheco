import RegistroCamper

def menu_camper():
    print("********************")
    print("Bienvenido Camper.")
    print("********************")
    accion = input("\n¿Qué deseas hacer?\n" +
                   "1. Registrarte.\n" +
                   "2. Actualizar estado.\n" +
                   "3. Reservar plaza en un parque.\n" +
                   "4. Cancelar reserva.\n" +
                   "5. Salir al menú principal.\n")

    if accion == "1":
        RegistroCamper.registrar_camper(RegistroCamper.campers)
    elif accion == "2":
        RegistroCamper.gestionar_estado_camper(RegistroCamper.camper)
    elif accion == "3":
        reservacion_plazas()
    elif accion == "4": 
        cancelar_reserva()
    elif accion == "5":
        main_menu()
    else:
        print('\nError, por favor elija una opción válida.\n')
        menu_camper()

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

