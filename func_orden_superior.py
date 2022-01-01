#Las funciones de orden superior son aquellas 
#que reciben como parametro a otra funcion 

#El metodo reduce debe ser importado de la libreria functools

from functools import reduce

def run():
    
    #filter y map comparten una misma estructura 
    #funcion, iterable
    my_list = [1,4,5,6,9,13,19,21]
    
    #filter permite filtrar los datos de una lista
    
    odd = list( filter(lambda x : x%2!=0, my_list))
    print(odd)
    
    #Map permite realizar una accion por cada elemento de la 
    #lista
    
    my_list2 = [1,2,3,4,5]
    squares = list( map(lambda i: i**2, my_list2) )
    print(squares)
    
    #Reduce permite iterar cada elemento de una lista
    #y devolver un elemento final 
    
    #reduce tiene una estructura distinta
    #funcion:  secuencia o accion, iterable
    my_list3 = [2,2,2,2,2]
    reducee = reduce(lambda a,b: a*b, my_list3)
    print(reducee)

if __name__ == "__main__":
    run()