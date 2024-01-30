def imprimirnombre ():
    nombre=str(input('Bienvenido, por favor ingresa tu nombre:\n'))
    print('Hola', nombre)
    return ""
 

def calculararea ():
    lado=int(input('Bienvenido, por favor ingresa la medida de los lados del cuadrado:\n'))
    area=lado**2
    print('El área del cuadrado es de:',area,'cm.')
    return ""
    

print(imprimirnombre())

print (calculararea())