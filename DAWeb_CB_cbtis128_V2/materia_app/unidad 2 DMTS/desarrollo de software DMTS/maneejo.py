#MANEJO DE LISTAS 

#crear una lista 
#lista numeros
numeros=[1,2,3,4,5,6,7,8,9,10]
print(numeros)
#lista de cadenas 
nombre=["raul","arturo","sofia","ana"]
print(nombre)

#aceder a los elemntos de una lista 
#indice 0 de numeros 
#mandamos a llamar la lista y entre corchetes el indice 
#deseado 
print(numeros[9])
print(nombre[0]),nombre[2]
print(nombre[1])

#modificar elementos de una lista 
#salida de nombres antes de la modificacion 
#raul arturo sofia ana 
nombre[1]="carlos"
#salida de nombres depues de modificacion 
#raul carlos sofia ana 
print(nombre)

#agregar elementos de una lista append
numeros.append(11)
numeros.append(12)
numeros.append(13)
numeros.append(14)
numeros.append(15)
print(numeros)

#metedo insert para agregar a una posicion 
#especifica
numeros.insert(1,"holis")
print(numeros)

#eliminar elementos de una lista 
#metodo remove 
numeros.remove("holis")
print(numeros)

#metodo pop eliminat por indice 
numeros.pop(14)
print(numeros)
numeros.pop(9)
print(numeros)

#recorrer una lista de datos 
#bucle for 

for var in numeros:
    print(var)

for variable in nombre:
    print(variable)

#verificar si un elemento se encuentra en lista 
if "luis" in nombre:
    print("luis si existe")
else:
    print("luis no existe:(")


#obtener una lista de nombres 
print(len(numeros))
print(len(nombre))

