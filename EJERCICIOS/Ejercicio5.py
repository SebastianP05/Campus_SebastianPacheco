def es_palindromo(palabra):
    
    palabra = palabra.lower()
    
    palabra = palabra.replace(" ", "")
    
    if palabra == palabra[::-1]:
        return True
    else:
        return False

palabra_ingresada = input("Ingresa una palabra: ")

if es_palindromo(palabra_ingresada):
    print(f"{palabra_ingresada} es un palíndromo.")
else:
    print(f"{palabra_ingresada} no es un palíndromo.")
