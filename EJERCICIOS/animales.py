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
        animales = list(cargarDatos)
        for i in animales:
            animales =  i
        id_animal=int(input("Digite el ID del Animal que desea Actualizar"))
        nombre=input("Nuevo Nombre: ")
        especie=input("Nueva Especie: ")
        edad=int(input("Nueva Edad: "))
        genero=input("Nuevo Genero: ")
        nuevoAnimal={'id':id_animal,'nombre':nombre, 'especie': especie, 'edad': edad, 'genero': genero}
        lista=list(map(lambda x : [x['id']==id_animal],animales))
        if any(lista):
            posicion=lista.index(True)
            animales[posicion]=nuevoAnimal
            guardarDatos(animales[:posicion]+[nuevoAnimal]+animales[posicion+1:])
            print ("Se ha actualizado correctamente.")
        else:
            print("No se encontró el animal con ese ID en la base de datos.")
    except Exception as e:
        print("Error al actualizar el animal: ",e)