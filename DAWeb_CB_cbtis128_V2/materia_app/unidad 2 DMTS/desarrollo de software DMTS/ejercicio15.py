#crear un codigo donde me parasca un menu operativo 
# uno es suma dos es resta tres multiplicacion y cuatro divicion 
#solicitar la informacion correspondiente al usuario 
print("1,suma")
print("2,resta")
print("3,multiplicacion")
print("4,divicion")
opcion=int(input("ingresa una de las operaciones para hacer tu opreacion"))
#funcion parametros 

def suma_numeros_paramtreos(a,b):
    suma=a+b
    return suma 
#termino funcional 
num1=int(input("ingresa el numero 1:"))
num2=int(input("ingresar el numero 2:"))
var=suma_numeros_paramtreos(num1,num2)
print("la suma es:",var)

#funcion parametros 
def resta_numeros_parametro(a,b):
    resta=a-b
    return resta 
#termino funcional 
num1=int(input("ingresa el numero 1:"))
num2=int(input("ingresar el numero 2:"))
var=resta_numeros_parametro(num1,num2)
print("la resta es:",var)

#funcion parametros 
def multiplicacion_numeros_paramtreos(a,b):
    multiplicacion=a*b
    return multiplicacion
#termino funcional 
num1=int(input("ingresa el numero 1:"))
num2=int(input("ingresar el numero 2:"))

var=multiplicacion_numeros_paramtreos(num1,num2)
print("la multiplicacion es:",var)

#funcion parametros 
def Divicion_numeros_paramtreos(a,b):
    Divicion=a/b
    return Divicion
#termino funcional 
num1=int(input("ingresa el numero 1:"))
num2=int(input("ingresar el numero 2:"))

var=Divicion_numeros_paramtreos(num1,num2)
print("la Divicion es:",var)

