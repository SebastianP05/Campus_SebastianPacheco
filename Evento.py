def registrar_participante(participantes_agosto):

    documento = input("Ingrese el número de documento del participante: ")
    nombre = input("Ingrese el nombre del participante: ")
    edad = input("Ingrese la edad del participante: ")
    cargo = input("Ingrese el cargo del participante: ")

    participante = {
        'documento': documento,
        'nombre': nombre,
        'edad': edad,
        'cargo': cargo,
        'pagado': False  # Nuevo campo para indicar si el participante ha pagado el aporte
    }

    participantes_agosto.append(participante)

    print("\nParticipante registrado para eventos en agosto:")
    print("Documento:", participante['documento'])
    print("Nombre:", participante['nombre'])
    print("Edad:", participante['edad'])
    print("Cargo:", participante['cargo'])
    print("Aporte pagado:", "Sí" if participante['pagado'] else "No")

    return participantes_agosto


def quitar_participante(participantes_agosto):
    documento_a_eliminar = input("Ingrese el número de documento del participante a eliminar: ")

    participante_encontrado = None
    for participante in participantes_agosto:
        if participante['documento'] == documento_a_eliminar:
            participante_encontrado = participante
            break

    if participante_encontrado:
        if not participante_encontrado['pagado']:
            participantes_agosto.remove(participante_encontrado)
            print(f"\nParticipante con documento {documento_a_eliminar} eliminado del registro.")
        else:
            print(f"\nNo se puede eliminar a un participante que ya ha pagado.")
    else:
        print(f"\nNo se encontró ningún participante con el documento {documento_a_eliminar}.")


def calcular_deuda(participantes_agosto):
    deuda_total = 0
    participantes_sin_pagar = []

    for participante in participantes_agosto:
        if not participante['pagado']:
            deuda_total += 50000
            participantes_sin_pagar.append(participante)

    print(f"\nTotal de participantes sin pagar: {len(participantes_sin_pagar)}")
    print(f"Deuda total acumulada: {deuda_total} COP")
    print("\nParticipantes sin pagar:")
    for participante in participantes_sin_pagar:
        print(f"Documento: {participante['documento']}, Nombre: {participante['nombre']}")


def registrar_evento(eventos):
    nombre_evento = input("Ingrese el nombre del evento: ")
    locacion_evento = input("Ingrese la locación del evento: ")
    dia_mes = input("Ingrese el día del mes para el evento: ")
    evento_realizado = input("¿El evento ya ha sido realizado? (Sí/No): ").lower() == 'sí'

    evento = {
        'nombre': nombre_evento,
        'locacion': locacion_evento,
        'dia_mes': dia_mes,
        'realizado': evento_realizado  
    }

    eventos.append(evento)

    print("\nEvento registrado:")
    print("Nombre:", evento['nombre'])
    print("Locación:", evento['locacion'])
    print("Día del mes:", evento['dia_mes'])
    print("Realizado:", "Sí" if evento['realizado'] else "No")

    return eventos


def gestionar_eventos(eventos):
    nombre_evento = input("Ingrese el nombre del evento que desea gestionar: ")

    evento_encontrado = None
    for evento in eventos:
        if evento['nombre'] == nombre_evento:
            evento_encontrado = evento
            break

    if evento_encontrado:
        print("\nEvento encontrado:")
        print("Nombre:", evento_encontrado['nombre'])
        print("Locación:", evento_encontrado['locacion'])
        print("Día del mes:", evento_encontrado['dia_mes'])
        print("Realizado:", "Sí" if evento_encontrado['realizado'] else "No")

        if not evento_encontrado['realizado']:
            accion = input("¿Desea eliminar (E) o modificar (M) el evento? ").upper()

            if accion == 'E':
                eventos.remove(evento_encontrado)
                print(f"\nEvento '{nombre_evento}' eliminado del registro.")
            elif accion == 'M':
                evento_encontrado['locacion'] = input("Ingrese la nueva locación del evento: ")
                evento_encontrado['dia_mes'] = input("Ingrese el nuevo día del mes para el evento: ")
                print(f"\nEvento '{nombre_evento}' modificado exitosamente.")
            else:
                print("\nAcción no reconocida. No se realizaron cambios.")
        else:
            print("\nNo se puede modificar o eliminar un evento ya realizado.")
    else:
        print(f"\nNo se encontró ningún evento con el nombre '{nombre_evento}'.")


def menu():
    participantes_agosto = []
    eventos_agosto = []

    while True:
        print('\nBienvenido a tu organizador de eventos\nLas opciones disponibles son:')
        print('1. Registrar participantes.')
        print('2. Registrar eventos.')
        print('3. Eliminar participantes.')
        print('4. Eliminar o modificar eventos.')
        print('5. Calcular deuda y participantes sin pagar.')
        print('6. Salir del sistema.')

        try:
            option = int(input('\nPor favor ingresa una opción: '))
        except ValueError:
            print('Por favor ingresa un número entero.')
            continue

        if option == 1:
            participantes_agosto = registrar_participante(participantes_agosto)
        elif option == 2:
            eventos_agosto = registrar_evento(eventos_agosto)
        elif option == 3:
            quitar_participante(participantes_agosto)
        elif option == 4:
            gestionar_eventos(eventos_agosto)
        elif option == 5:
            calcular_deuda(participantes_agosto)
        elif option == 6:
            if confirmar_salida():
                print('\nSaliendo del sistema.')
                break
        else:
            print('Selecciona una opción válida.')
        
        input('\nPresiona Enter para continuar...')

menu()

