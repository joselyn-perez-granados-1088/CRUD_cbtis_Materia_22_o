#EJERCICO DE NUMERO MAYOR Y MENOR 
#VARIABLE
#NumeroMyoryMenor 

def evaluar_si_es_mayor_menor():
    try:#declaramos variables 
        #solicitamos el ingreso de informacion 
        #y convertimos 
        num1=int(input("ingresa numero 1:"))
        num2=int(input("ingresa numero 2:"))
       #
        if num1>num2:
            print("num1 es mayor:")
        elif num1<num2:
            print("num2 es menor:")
        elif num1==num2:
            print("son iguales")
        else:
            print("el numero es cero")
    except ValueError:
            print("error")
evaluar_si_es_mayor_menor()
    
        




        
