def divisors(num):
    divisor = [i for i in range(1,num+1) if num%i==0]
    return divisor

def run():
    num = int(input("Ingrese un numero: "))
    print(divisors(num))
    print("Termino mi programa")

if __name__ == "__main__":
    run()