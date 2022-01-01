
def main():
    # squares = []
    # for i in range(1, 101):
    #     if i%3!=0:
    #         squares.append(i**2)
    # print(squares)
    
    # iterador, ciclo, condicional
    squares = [i**2 for i in range(1,101) if i%3 != 0]
    print(squares)
    
    multiplos_cuatro = [i for i in range(1, 100000) if i%36 == 0]
    print(multiplos_cuatro)


if __name__ == "__main__":
    main()