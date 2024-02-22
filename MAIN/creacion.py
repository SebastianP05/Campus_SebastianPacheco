import json

def ver_menu():
    try:
            
        print ("El menú que tenemos disponible el día de hoy es:")
        print ("*************************************************")

        
        entrada={"Empanadas_Mini": 9000, "Papas_Fritas": 5000, 
                    "Dedos_de_Queso": 11000, "Tostada_Francesa": 10000}
        
        plato_fuerte={"Pasta Bolognesa": 35000, "Hamburguesa": 28000, 
                    "Pollo_al_curry": 30000, "Lechona": 25000, "Arroz_al_wok": 20000}
        
        bebida={"Coca_Cola" : 3000, "Jugo_Natural": 5000, 
                    "Vino": 8000, "Cerveza": 3500}

        print ("Entradas: ", entrada)
        print ("Platos Fuertes: ", plato_fuerte)
        print ("Bebidas: ", bebida)
    except Exception:
        print ("********************************")
        print ("No se ha podido mostrar el menú.")
        print ("********************************")

def crear_pedido(pedidos, nombre_archivo):
    
    try: 
        numero = input("Ingrese el número de su pedido:" )
        entrada = input("Ingresa el nombre de la entrada: ")
        cantidadEnt= int(input("Ahora la cantidad: "))
        plato_fuerte = input("Ingrese el nombre del plato fuerte: ")
        cantidadPF = int(input("Ahora la cantidad: "))
        bebida = input("Ingrese el nombre de la bebida: ")
        cantidadBebida = int(input("Ahora la cantidad: "))

        pedido = {
            'numero': numero,
            'entrada': entrada,
            'cantidadEnt': cantidadEnt,
            'plato_fuerte': plato_fuerte,
            'cantidadPF': cantidadPF,
            'bebida': bebida,
            'cantidadBebida': cantidadBebida,
            'Estado': 'Creado',
            'Pagado': 'no',
        }

        pedidos.append(pedido)
        
        print("***************************")
        print("Pedido creado exitosamente.")
        print("***************************")
        print("numero:", pedido['numero'])
        print("entrada:", pedido['entrada'])
        print("cantidadEnt:", pedido['cantidadEnt'])
        print("plato_fuerte:", pedido['plato_fuerte'])
        print("cantidadPF:", pedido['cantidadPF'])
        print("bebida:", pedido['bebida'])
        print("cantidadBebida:", pedido['cantidadBebida'])
        print("Estado:", pedido['Estado'])
        print("Pagado:", pedido['Pagado'])
         
        with open(nombre_archivo, 'w') as file:
            json.dump(pedidos, file)

        return pedidos
    
    except Exception:
        print("************************************")
        print("No se pudo crear el pedido")
        
