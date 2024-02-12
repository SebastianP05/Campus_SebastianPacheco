import json

paises=[
    {
        "Pais": "Colombia",
        "Continente": "SurAmérica",
        "Moneda": "Peso Colombiano",
        "Lenguaje": "Español",
        "Capital": "Bogotá"
    },{
        "Pais": "Argentina",
        "Continente": "SurAmérica",
        "Moneda": "Peso Argentino",
        "Lenguaje": "Español",
        "Capital": "Buenos Aires"
    },{
        "Pais": "Venezuela",
        "Continente": "SurAmérica",
        "Moneda": "Bolívar Venezolano",
        "Lenguaje": "Español",
        "Capital": "Caracas"
    },{
        "Pais": "Perú", 
        "Continente": "SurAmérica",
        "Moneda": "Sol Peruano",
        "Lenguaje": "Español",
        "Capital": "La Habana"
    }
]

archivo="paises.json"

with open(archivo, 'w') as file:
        json.dump(paises, file)


with open ('Paises.json', 'r') as paises_file:
    data_paises = json.load(paises_file)

for pais in data_paises : 
      print ("País: ", pais["Pais"])
      print ("Continente:", pais["Continente"])
      print ("Moneda:", pais["Moneda"])
      print ("Lenguaje:", pais["Lenguaje"])
      print ("Capital:",  pais ["Capital"])
      print ("-------------------------------")