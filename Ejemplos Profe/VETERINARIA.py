import json
datos = []

def cargarDatos():
    with open("veterinariaBD.json", "r") as file:
        respuesta = json.load(file)
        return respuesta

def guardarDatos(datos):
    with open("veterinariaBD.json", "w") as file:
        escritura = json.dumps(datos, indent=4)
        file.write(escritura)

def crearAnimal():    
    try:
        animales = list(cargarDatos())    
        tipo = input("Ingrese el tipo de animal: ")
        nPatas = int(input("Ingrese el numero de patas del animal: "))
        raza = input("Ingrese la raza del animal: ")
        animal = {"tipo": tipo, "nPatas": nPatas, "Raza": raza}
        animales.append(animal)
        guardarDatos(animales)
        print("Animal creado con éxito!")
    except Exception:
        print("Ocurrió un error al crear animal!")

def eliminarAnimal():
    try:
        animales = list(cargarDatos())
        for i in range(len(animales)):
            print(str(i),"->",animales[i])
        opc = int(input("Ingrese el número del animal a borrar: "))
        animales.pop(opc)
        guardarDatos(animales)
        print("Animal borrado con éxito!")
    except Exception:
        print("Ocurrió un error al borrar animal!")
    

def mostrarAnimal():
    try:
        animales = list(cargarDatos())
        for i in range(len(animales)):
            print(str(i),"->",animales[i]["tipo"])
        opc = int(input("Ingrese el número del animal a mostrar: "))
        print(animales[opc])
    except Exception:
        print("Ocurrió un error al mostrar animal!")

def mostrarTodosLosAnimales():
    try:
        animales = list(cargarDatos())
        for i in range(len(animales)):
            print(str(i),"->",animales[i])
    except Exception:
        print("Ocurrió un error al mostrar animal!")

def actualizarAnimal():
    try:
        animales = list(cargarDatos())
        for i in range(len(animales)):
            print(str(i),"->",animales[i])
        opc = int(input("Ingrese el animal a actualizar: "))
        animal = animales[opc]
        print("El tipo del animal actual es",animal["tipo"])
        tipo = input("Ingrese el tipo de animal: ")
        print("El número de patas del animal actual es",int(animal["nPatas"]))
        nPatas = int(input("Ingrese el numero de patas del animal: "))
        print("La raza del animal actual es",animal["Raza"])
        raza = input("Ingrese la raza del animal: ")
        animal = {"tipo": tipo, "nPatas": nPatas, "Raza": raza}
        animales[opc] = animal
        guardarDatos(animales)
        print("Animal actualizado con éxito!")        
    except Exception:
        print("Ocurrió un error al actualizar animal!")
