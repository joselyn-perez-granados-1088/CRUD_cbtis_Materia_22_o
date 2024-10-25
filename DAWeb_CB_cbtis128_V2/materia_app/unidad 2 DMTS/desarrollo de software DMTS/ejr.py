#ejercicio 11
#declaracion de funcion 
def promedio():
    try: 
        cali1=int(input("ingrese la primera calificacion"))
        cali2=int(input("ingrese la segunda calificacion"))
        cali3=int(input("ingrese la tercera calificacion"))
        #reliza operacion 
        prom=(cali1+cali2+cali3)/3

        #determinar cual es el mayor y menor
        mayor=max(cali1,cali2,cali3)
        menor=min(cali1,cali2,cali3)
        #imprimir resultado
        return ("el promedio es",prom,"mayor:",mayor, "menor:",menor)
    except ValueError:
        return "error: ingrese valores numericos"




#termina funcion 

#mandar a llamar a funcion 
resultado=promedio()
print(resultado)
