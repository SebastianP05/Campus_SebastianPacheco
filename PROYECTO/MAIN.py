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

main_menu()
