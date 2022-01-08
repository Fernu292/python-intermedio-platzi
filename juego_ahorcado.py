import random
import os

def getLetra():
    character = input("\nDigita una letra: ")
    if character.isnumeric():
        raise ValueError("Introduce solo datos tipo caracter")
        getLetra()
    return character

def ahorcado():
    palabras = []
    
    with open("./data/palabras.txt", "r", encoding="utf-8")as f:
        palabras = [palabra for palabra in f]
        
    palabra = palabras[random.randint(0, len(palabras)-1)]
    letras = ""
    
    for c in palabra:
        letras+="_ "
    print(letras)
    letra = getLetra()
    
   

    
def run():
    try:
        print("\n****** Bienvenido al juego del ahorcado ******\n")
        ahorcado()
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    run()