import json

def cambiar_estado(numero, nombre_archivo):
    
    try:
        nombre_archivo='pedidos.json'

        with open(nombre_archivo, 'r') as file:
            pedidos = json.load(file)

        pedido_encontrado = None
        for pedido in pedidos:
            if pedido['numero'] == numero:
                pedido_encontrado = pedido
                break

        if pedido_encontrado is not None:
            print("***************************")
            print("Estados disponibles:")
            print("1. En preparacion.")
            print("2. Servido")
            print("3. Cancelado")

            opcion = input("Ingrese el número correspondiente al nuevo estado: ")

            estados = {
                '1': 'En preparacion',
                '2': 'Servido',
                '3': 'Cancelado',
            }

            nuevo_estado = estados.get(opcion, 'Estado no válido')

            if nuevo_estado != 'Estado no válido':
                pedido_encontrado['Estado'] = nuevo_estado
                print("Estado actualizado exitosamente.")
            else:
                print("Opción no válida. El estado no ha sido actualizado.")
        else:
            print(f"No se encontró un pedido con el número {numero}.")

        with open(nombre_archivo, 'w') as file:
            json.dump(pedidos, file)
            
    except IOError:
        print("No se encontró un pedido con el número {numero}.")

def pagar_pedido(numero, nombre_archivo):
    
    try:
     
        nombre_archivo='pedidos.json'
        
        with open(nombre_archivo, 'r') as file:
            pedidos = json.load(file)

        pedido_encontrado = None
        for pedido in pedidos:
            if pedido['numero'] == numero:
                pedido_encontrado = pedido
                break

        if pedido_encontrado is not None:
            print("***************************")
        
            pago = input("Ya está pagado el pedido?(1.Sí/2.No): ")
        
            Pagado = {
            '1': 'Si',
            '2': 'No',
            }
            nuevo_pago = Pagado.get(pago, 'Error')

            if nuevo_pago != 'Error':
                pedido_encontrado['Pagado'] = nuevo_pago
                print("Pago registrado exitosamente.")
            else:
                print("Opción no válida. El pago no ha sido registrado.")
        else:
            print(f"No se encontró un pedido con el número {numero}.")

        with open(nombre_archivo, 'w') as file:
            json.dump(pedidos, file)
            
    except Exception:
        print("No se encontró un pedido con el número {numero}.")