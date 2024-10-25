#EJERCICIO 10- par, impar y cero 
#.variables 
#funciones 
#operacion(condiciones)
#imprimir resultado o mandar mensaje 
#funcion sin parametro 
#VRIABLE 
#solicitando el numero con input()
#convirtiendo entero con int()

#def evaluacion_de_numero():
#VRIABLE 
#solicitando el numero con input()
#convirtiendo entero con int(
 #numero=int(input("ingresa el numero a veñuar:"))
#condicion 
 #if numero == 0:
  #print("el numero es par")
# elif  numero % 2==0:
 # print("el numero es igual a cero")
 #else:
  #print("el numero es impar")

#termina funcion 
#funcion con parametro 
def evaluar_par_impar(a):
 if a == 0:
  return"el numero es par"
 elif  a % 2==0:
  return"el numero es igual a cero"
 else:
  return"el numero es impar"
#termina funcion 
num_solicitado=int(input("ingresa:"))
resultado=evaluar_par_impar(num_solicitado)
 
print(resultado)
