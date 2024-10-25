#crear un codigo donde se solicite al usuario ingresar el numero 
# correspondiente al dia de la semana, 

#declaramos funcion 
def dia_de_la_seman():
    try:
        a=int(input("ingresa el numero del 1-7:"))
        if a==1:
            print("lunes")
        elif a==2:
            print("martes")
        elif a==3:
            print("miercoles")
        elif a==4:
            print("jueves")
        elif a==5:
            print("viernes")
        elif a==6:
            print("sabado")
        elif a==7:
            print("domingo")
        else:
            print("numero incorrecto")
    except ValueError:
        print("error: no puedes digitar cadena de texto")
    
dia_de_la_seman()


