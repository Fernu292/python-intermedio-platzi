def divisors(num):
    if num < 0:
        raise ValueError("Ingresa un valor positivo")
    divisor = [i for i in range(1,num+1) if num%i==0]
    return divisor

def run():
    try: 
        num = int(input("Ingrese un numero: "))
        print(divisors(num))
        print("Termino mi programa")
    #Atrapar errores difiniendolo como ve
    except ValueError as ve: 
        print(ve)
        run()
        
if __name__ == "__main__":
    run()