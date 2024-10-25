#crear un codigo que se solicite tres numeros 
#validar cual de ellos es  es el mayor, si som iguales o si es igual a cero 
def mayor_tres_numeros():
    try:
        #declaracion variables 
        #solicitadas el ingresar de informacion 
        #y convertir 

        numero1=int(input("ingresr el primer numero:"))
        numero2=int(input("ingresar el segundo numero:"))
        numero3=int(input("ingresar el trecer numero:"))
    
    #variable que los numeros sean iguales 
        if numero1==numero2==numero3:
            return "Los numeros son iguales "
    #validar cual de los numeros es cero 
        elif numero1== 0 or  numero2==0 or numero3==0: 
            return "Uno de los numeros es 0"
    #mayor o menor  
        else:
        #Validar el mayor de tres numeros 
            if numero1>numero2:
                return"el numero",numero1,"es mayor a",numero2,numero3
            elif numero2>numero3:
                return"el numero",numero2,"es mayor a",numero3,numero1
            else:
                return"el numero",numero3, "es mayor a",numero1,numero2
    except ValueError:
            return"error: no puedes ingresar cadena de texto"
#llamar la funcion 
resul=mayor_tres_numeros()
#imprimir resultado por return
print(resul)
