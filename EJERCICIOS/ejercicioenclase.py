def clasificar_palabra(palabra):
    longitud = len(palabra)
    
    if longitud < 5:
        return 'corta'
    elif 5 <= longitud <= 10:
        return 'media'
    else:
        return 'larga'

palabra_ingresada = input("Ingresa una palabra: ")

clasificacion = clasificar_palabra(palabra_ingresada)
print(f"La palabra '{palabra_ingresada}' es una palabra {clasificacion}.")
