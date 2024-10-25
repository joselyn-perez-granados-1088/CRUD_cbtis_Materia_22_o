#ejercicio 13 positivo negativo 

def evaluar_numero():
    try:
        #decalracion de variables 
        #solicitamos informacion 
        #y convertimos 
        numero=int(input("ingresa el numero"))
        #variables si el numero es cero 
        if numero==0:
            return"el numero es cero"
        #evaluar si el numero es positivo 
        elif numero>0:
            return "el numero es positivo"
        else:
            return "el numero es negativo"
    except ValueError:
            return "error:no se puede ingresar la cadena de texto"

#terminar funcion 

#mandar a llamar la funcion 
resul= evaluar_numero()
print(resul)




    
    