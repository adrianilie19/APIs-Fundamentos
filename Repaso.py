import requests
import random

apiSimpson = "https://thesimpsonsquoteapi.glitch.me/quotes"

contenido = requests.get(apiSimpson)
personaje = contenido.json()

if personaje:
    quote = personaje[0]["quote"]
    respuesta = personaje[0]["character"]

    print(f"Frase: {quote}")
    personajIntroducido = input("Tu repuesta es: ")

    if personajIntroducido == respuesta:
        print("¿Acertaste!")
    else:
        print(f"El personaje era: {respuesta}")
