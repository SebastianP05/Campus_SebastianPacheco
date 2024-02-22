import json

def main_menu():

    try:
    
        print("********************************************")
        print("Bienvenido a tu restaurante Monopollito.")
        print("**********************************************")
        print("Por el momento solo tenemos  estas opciones:")
        print("**********************************************")

        while True:
            opcion = int(input("\n1. Creación de pedidos.\n" +
                            "2. Información de pedidos.\n"+
                            "3. Gestion de pedidos.\n" +
                            "4. Salir.\n"
                            "\n¿A qué opcion deseas acceder?\n"
                            ":"
                            ))
            if opcion == 1:
                creacion_de_pedidos()
            elif opcion == 2:
                info_pedido()
            elif opcion == 3:
                gestion_pedido()
            elif opcion == 4:
                salir = input("¿Quieres salir del programa? (Sí/No): ").lower()
                if salir=='si':
                    break
                    
            else:
                print ("************************************")
                print("Opción no válida. Inténtalo de nuevo.")
                print ("************************************")
                
    except KeyboardInterrupt:
        print("******************************************")
        print("No haz seleccionada ninguna opción valida.")
        print("******************************************")
        main_menu()    
                
    

def creacion_de_pedidos():
    
    try:
        
        print("***********************************")
        print("Bienvenido a tu creador de pedidos.")
        print("***********************************")
            
        while True:
            accion = int(input("¿Qué deseas hacer?\n" +
                            "\n1. Ver el menú.\n" +
                            "2. Crear un pedido.\n" +
                            "3. Salir al menú principal.\n"))
            
            if accion == 1:
                print("**********************************************")
                ver_menu()
                print("************************************")
                volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
                if volver_al_menu != 'si':
                    break
            
            elif accion == 2:
                print("*******************************************")
                print("Para crear el pedido necesito estos datos:\n")
                print("*******************************************")
                pedidos=[]
                nombre_archivo='pedidos.json'
                crear_pedido(pedidos,nombre_archivo)
                print("************************************")
                volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
                if volver_al_menu != 'si':
                    break
            
            elif accion == 3:
                main_menu()
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                
    except KeyboardInterrupt:
        print("************************************")
        print("Has interrumpido el proceso de pedidos.")
        print("************************************")
        main_menu()            

from creacion import ver_menu
from creacion import crear_pedido

def info_pedido():
    
    try:
        
        print("**********************************************")
        print("Bienvenido, que quieres saber de tu pedido.")
        print("**********************************************")
            
        while True:
            accion = int(input("\n1. Ver el estado del pedido.\n" +
                            "2. Consultar los pedidos creados.\n" +
                            "3. Consultar los pedidos pagados.\n" +
                            "4. Consultar los pedidos servidos.\n" +
                            "0. Salir al menú principal.\n"))
            
            if accion == 1:
                print("**********************************************")
                #ver_menu()
                
            elif accion == 2:
                
                print("************************************")
                pedidos=[]
                consultar_pedidos_creados(pedidos)
                volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
                if volver_al_menu != 'si':
                    break
                
            elif accion == 3:
                
                print("************************************")
                pedidos=[]
                consultar_pedidos_pagados(pedidos)
                volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
                if volver_al_menu!='si':
                    break
                
            elif accion == 4:
                
                print("************************************")
                pedidos=[]
                consultar_pedidos_servidos(pedidos)
                volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
                if volver_al_menu!='si':
                    break
                    
            elif accion == 0:
                main_menu()
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                
    except Exception:
        print ("************************************")
        print("Error, intenta nuevamente.")
        print ("************************************")

from Informacion import consultar_pedidos_creados
from Informacion import consultar_pedidos_pagados
from Informacion import consultar_pedidos_servidos

def gestion_pedido():
    
    try:
        
        print("**********************************************")
        print("Bienvenido, que quieres hacer con tu pedido.")
        print("**********************************************")
            
        while True:
            accion = int(input("\n1. Cambiar el estado del pedido.\n" +
                            "2. Pagar el pedido.\n" +
                            "3. Salir al menú principal.\n"))
            
            if accion == 1:
                
                print("******************************")
                numero = input("Ingrese el número del pedido que desea gestionar: ")
                print("**********************************************************")
                nombre_archivo='pedidos.json'
                cambiar_estado(numero, nombre_archivo)
                print("******************************")
                volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
                if volver_al_menu != 'si':
                        break    
                
            elif accion == 2:
                
                print("******************************")
                numero = input("Ingrese el número del pedido que desea pagar: ")
                print("**********************************************************")
                nombre_archivo='pedidos.json'
                pagar_pedido(numero, nombre_archivo)
                volver_al_menu = input("¿Quieres volver al menú? (Sí/No): ").lower()
                if volver_al_menu != 'si':
                    break
            
            elif accion == 3:
                main_menu()
                
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                
    except Exception:
        print ("************************************")
        print("Error, intenta nuevamente.")
        print ("************************************")

from gestion import cambiar_estado
from gestion import pagar_pedido
                