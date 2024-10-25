#funcion definidas por el usuario 
#decalramos funcion 
#sintaxis:def <nombre funcion> (parametros)

def saludar(): 
    print("!holis!!!")

#Mandando a llamar a mu funcio a saludar 
saludar()

#Funcion de parametros 
#Decalramos la funcion 
def saludar_persona(nombre):
    #mandamos mensaje concatenado variable cadena 
     print("Hola!",nombre,"como estas?")
#mandar mensaje sin concatenacion 
     #print("Hola! {nombre}!!, como estas?")
#mandar a llamr a funcion y pasar psrametro 
saludar_persona("Paco")

#Funcion con multiples parametros

def sumar (a,b):
   return a+b
#variable rssultado 
resultado=sumar(3,5)
#imprimimos mensaje con el resultado de la suma 
     print("la suma es:",resultado)#salida:8

#funcion con valor por defecto 
def saludar_profesor (nombre,titulo="Sr./Sra")
    print("hola",titulo,"",nombre)
    #solo mandamos el parametro nombre 

saludar_profesor("jose")
#mandamos el paranmbre y nodificamos el titulo 
saludar_profesor("francico","Dr.")

#funcion de devuelve multiples de valores 
def operaciones(a,b)
    suma=a+b
    resta=a-b
    multi=a*b
    div=a/b
        #1 #2 #3 #4
    return suma,resta,multi,div
#el orden de daclarar de variable debe ser igual al orden del resturn 
resul_suma,resul_resta,resul_multi,resuñ_div=operaciones (10,2)

print("la suma es:",resul_suma)
print("la resta es:",resul_resta)
print("la multiplicaciones es:",resul_multi)
print("la diviciones es:",resul_div)



