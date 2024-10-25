#crear un codigo que permita generar la tabla de multiplicar del 1 al diez a partir del numero que ingrese el usuario 
def tabla_de_multiplicar():
    try:
        numero=int(input("digita un numero del 1 al 10:"))

    
        for i in range (1,11):
            print("la tabla de multiplicar es")
            print(numero,"x",i,"=",numero*i)
    except ValueError:
            print("error")



tabla_de_multiplicar()
