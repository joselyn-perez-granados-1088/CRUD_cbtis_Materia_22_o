#crear un codigo que imprima los numeros del 100 al 1 a demas de que imprima la suma de lo numeros del 1 al 100 
#crear un codigo que imrpima la suma de los pares e impares del 1 al 100 

def secuencia():
    try:
        #decalrar e inicializar a 0
        suma=0
        #se imrprime los numeros del 100 al 1
        for numero_del_ciclo in range (100,0,-1):
            #1. imrprimir los numeros 
            print(numero_del_ciclo)
            #2. suam de los numeros 
            suma+=numero_del_ciclo
            #3.mostrar la suma
        print("la suma de los numeros es:",suma)
    except SyntaxError:
        print("error en el sistema")
secuencia()
