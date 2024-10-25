#manejo de eerores en prthon 
#ZeroDivicionEntera
def verificar_divicion(a,b):
    #es el codigo que se ejecuta y se tiene que verificar
    #en caso de error
    try:  
        resul=a/b
        return resul
    #ecepto indicamos el tipo de eeror a manejar y 
    #lo que ocurre durante el eeror
    except ZeroDivisionError:
        return "Error: estas tratando de dividir entre cero"
    #termina fucion

    #decalracion 
num1=10
num2=0
resultado=verificar_divicion(num1,num2)
print(resultado)


