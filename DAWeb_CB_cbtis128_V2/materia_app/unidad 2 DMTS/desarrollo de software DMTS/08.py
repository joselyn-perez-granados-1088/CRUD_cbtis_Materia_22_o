#crear un codigo que imrpima la suma de los pares e impares del 1 al 100 
def SERIE():
    try:
        #al usar contadores es necesario decalarar variables e inicializae a 0
        par =0
        impar=0

        #se va a repitir el 100 veces la informaciion correspondiente
        for i in range (1,101):
            #1. imprimir los numeros del 1 al 100
                #2.suma de pares
            if i%2==0:
                #cuando el numero sea par 
                #operador de asignacion +=
                par+=i
                #ciclo / valor    / numero ciclo 
                #1       0             1
                #2         2            2
                #4        6             4
            else:
                #cuando el numero sea impar 
                impar += i 
        print("la suma de los paresa es:",par)
        print("la suma de los impares es:",impar)
    except SyntaxError:
        print("error en el sistema")
SERIE()