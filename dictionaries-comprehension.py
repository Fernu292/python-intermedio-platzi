def main():
    #Llave: elemento ciclo condicional
    # diccionario = {i : i**2 for i in range(1,101) if i%3!=0}
    diccionario = {i: round(i**0.5, 2) for i in range(1,1001)}
    print(diccionario)

if __name__ == "__main__":
    main()