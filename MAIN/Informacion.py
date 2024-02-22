import json

def consultar_pedidos_servidos(pedidos):
    pedidos_servidos = [pedido for pedido in pedidos if pedido['Estado'] == 'Servido']
    
    if not pedidos_servidos:
        print("No hay pedidos servidos.")
    else:
        print("Los pedidos ya servidos son:")
        for pedido in pedidos_servidos:
            print(f"- {pedido['Estado']} (numero: {pedido['numero']})")

def consultar_pedidos_creados(pedidos):

    pedidos_creados = [pedido for pedido in pedidos if pedido['Estado'] == 'Creado']
    print("Los pedidos ya creados son:")
    for pedido in pedidos_creados:
        print(f"- {pedido['Estado']} (numero: {pedido['numero']})")

def consultar_pedidos_pagados(pedidos):
    
    pedidos_pagados = [pedido for pedido in pedidos if pedido['Pagado'] == 'si']
    print("Los pedidos que ya están pagos son:")
    for pedido in pedidos_pagados:
        print(f"- {pedido['Pagado']} (numero: {pedido['numero']})")



