
#Las funciones anonimas son de una sola linea de codigo
#Ademas se especifican con la palabra reservada lambda
#Estas funciones anonimas tienen un return implicito
def run():
    
    palindromo = lambda string : string == string [::-1]
    
    print(palindromo('ana'))

if __name__ == '__main__':
    run()