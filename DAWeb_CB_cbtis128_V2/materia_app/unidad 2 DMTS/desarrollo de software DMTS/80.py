#manejo de eerores en python 
#IndexError

def acceso_lista(lista,indice):
    try:
        dato=lista[indice]
        return "dato en la pocicion ", indice , "es" ,dato
    except IndexError:
        return "Error: el indice esta fuera de rango"
    #termina funcion 

#decalracion de listsa 
lista=[10,20,30,40,50]
indice=int(input("ingrese el indice al que quieres acceder es:"))
print(acceso_lista(lista,indice))