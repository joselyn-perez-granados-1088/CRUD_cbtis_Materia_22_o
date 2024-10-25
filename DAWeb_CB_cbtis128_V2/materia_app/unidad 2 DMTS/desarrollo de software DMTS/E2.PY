#Ejercicio 2 suma de dos numeros con funciones 
#1.variables 
#2.funciones 
#3.opreaciones 
#4.imprimir resultado mandar mensaje 
#funcion sin parametros 
#def suma_numeros():
#pedimos informacion y guardamos variable 
#num1=int(input("ingresa el numero 1:"))
#num2=int(input("ingresar el numero 2:"))
#suma=num1+num2 
#print("la suma es.",suma)
#suma_numeros()

#funcion parametros 
def suma_numeros_paramtreos(a,b):
    suma=a+b
    return suma 
#termino funcional 
num1=int(input("ingresa el numero 1:"))
num2=int(input("ingresar el numero 2:"))

var=suma_numeros_paramtreos(num1,num2)
print("la suma es:",var)

