def divisors(num):
    divisor = [i for i in range(1,num+1) if num%i==0]
    return divisor

def run():
    
    num = input("Ingrese un numero: ")
    
    #Assert funciona con una condicion, mensaje de error
    assert int(num) > 0,"Ingresa valores positivos" 
    assert num.isnumeric(), "Debes ingresar datos numericos" # Retorna si un string es tipo numerico
    print(divisors(int(num)))
    print("Termino mi programa")
    
        
if __name__ == "__main__":
    run()