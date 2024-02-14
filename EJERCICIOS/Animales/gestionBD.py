import json

def cargarDatos(archivo):
    with open(archivo, "r") as file:
        try:
            respuesta = json.load(file)
            return respuesta
        except Exception:
            return []
        

def guardarDatos(datos, archivo):
    with open(archivo, "w") as file:
        escritura = json.dumps(datos, indent=4)
        file.write(escritura)