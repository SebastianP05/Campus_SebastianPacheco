

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
    rol=input("Por favor elige tu rol: ")

    if rol == 1:
        menu_camper()
    elif rol == 2:
        menu_trainer()
    elif rol == 3:
        memu_coordinador()
    else:
        print('********************************')
        print('Error, elije una opción valida.')
        print('********************************')
        rol=input("Por favor elige tu rol: ")

main_menu()

def menu_camper():
    print("********************")
    print("Bienvenido Camper.")
    print("********************")
    accion = input("\n¿Qué deseas hacer?\n" +
                   "1. Registrarte.\n" +
                   "2. Buscar un parque.\n" +
                   "3. Reservar plaza en un parque.\n" +
                   "4. Cancelar reserva.\n" +
                   "5. Salir al menú principal.\n")

    if accion == "1":
        registrar_camper(campers)
    elif accion == "2":
        busqueda_parque()
    elif accion == "3":
        reservacion_plazas()
    elif accion == "4": 
        cancelar_reserva()
    elif accion == "5":
        main_menu()
    else:
        print('\nError, por favor elija una opcion valida.\n')
        menu_camper()

def ver_parques(sort="nombre", order="asc"):
    # Mostrar todos los parques ordenados por nombre ascendentemente
    campers.ordenar_por(sort, order)
    for i in range(len(campers)):
        print(str(i+1)+". "+campers[i].getNombre())
    print()
    accion = input("Presione Enter para continuar o 's' para volver al menú principal:\n")
    if accion=="s":
        main_menu()
    else:
        menu_camper()

def busqueda_parque():
    criterio = input("\nIngrese el criterio de búsqueda (criterio, ciudad, pais): ")
    valor = input("Ingrese el valor a buscar: ")
    resultado = camperos.buscar(criterio, valor)
    if len(resultado)>0:
        print("\nResultados de búsqueda:")
        for i in range(len(resultado)):
            print(str(i+1)+". "+resultado[i].mostrar())
        accion = input("\nPresione Enter para continuar o 's' para volver al menú principal:\n")
        if accion!='s':
            menu_camper()
        else:
            main_menu()
    else:
        print("\nNo se encontraron resultados.")
        input("Presione Enter para continuar...\n")
        menu_camper()

def reservar_plaza(id_parque):
    plazas_disponibles = camperos[id_parque-1].getPlazasDisponibles()
    if plazas_disponibles>0:
        fecha_inicio = input("\nFecha de inicio (dd/mm/aaaa): ")
        try:
            validacion = datetime.datetime.strptime(fecha_inicio, '%d/%m/%Y').date()
            while True:
                fecha_fin = input("Fecha de finalización (dd/mm/aaaa): ")
                try:
                    validacion2 = datetime.datetime.strptime(fecha_fin, '%d/%m/%Y')
                    if validacion <= validacion2.date():
                        break
                    else:
                        print("La fecha de finalización debe ser posterior a la de inicio.\nIntente nuevamente.")
                except ValueError:
                    print("Formato incorrecto. Por favor ingrese una fecha en dd/mm/aaaa.")
            clientes = Clientes()
            nombre = input("\nNombre del cliente: ")