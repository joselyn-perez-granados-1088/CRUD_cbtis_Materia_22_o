import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
#--------variable global
#son variables globales por que en caso de requerirlas las mandamos a llamar
#las variables tienen que ser decalradas e iniciadas
var_num1=0
var_operacion=0
#var_operacion =1 - suna 
#var_operacion =2 -resta
#var_operacion=3 -mult
#var_operacion=4 - div
#var_operacion =5 -poercentaje 
#funcion salir 
#define el proceso de la vemtama principal y cerrrar el programa 
def salir():
    ventana_principal.quit()

#Funcion de pantalla principal 
def pantalla_s():
    ventana_principal.geometry("300x200")

def pantalla_m():
    ventana_principal.geometry("600x400")

def pantalla_g():
    ventana_principal.geometry("1020x800")

def uno():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor actual y numero correspondinte 
    entrada1.insert(tk.END,valor_actual+"1")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def dos():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor 1
    entrada1.insert(tk.END,valor_actual+"2")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def tres():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor 1
    entrada1.insert(tk.END,valor_actual+"3")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def cuatro():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor 1
    entrada1.insert(tk.END,valor_actual+"4")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def cinco():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor 1
    entrada1.insert(tk.END,valor_actual+"5")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def seis():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor 1
    entrada1.insert(tk.END,valor_actual+"6")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def siete():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor 1
    entrada1.insert(tk.END,valor_actual+"7")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def ocho():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor 1
    entrada1.insert(tk.END,valor_actual+"8")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def nueve():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor 1
    entrada1.insert(tk.END,valor_actual+"9")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def cero():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor 1
    entrada1.insert(tk.END,valor_actual+"0")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def punto():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #obtener el valor actual
    valor_actual=entrada1.get()
    #borrar entrada
    entrada1.delete(0,tk.END)
    #insetamos el valor 1
    entrada1.insert(tk.END,valor_actual+".")
    #desabilitar con readonly
    entrada1.config(state="readonly")

def suma():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #mandar a llamar las variables globales
    global var_num1
    global var_operacion
    #obtener y convertir el valor de la entrada
    num1=float(entrada1.get())
    #borrar entrada para ingresar num2
    entrada1.delete(0,tk.END)
    #guardar el valor obtenido de entrada en variable var_num1 para hacer uso del valor igual 
    var_num1=num1
    #guardar el valor obtenido de entrada en variable var_operacion para hacer uso del valor igual 
    var_operacion=1 
    entrada1.config(state="readonly")

def resta():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #llamar las variables globales 
    global var_num1
    global var_operacion
    #obtener y convertir el valor  de la entrada
    num1=float(entrada1.get())
    #borrar entrada para ingresar num2
    entrada1.delete(0,tk.END)
    #guardar el valor obtenido de entrada en variable var_num1 para hacer uso del valor igual 
    var_num1=num1
    #guardar el valor obtenido de entrada en variable var_operacion para hacer uso del valor igual 
    var_operacion=2
    #cambiar propiedad de entrada a lectura
    entrada1.config(state="readonly")

def multiplicacion():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #llamar las variables globales 
    global var_num1
    global var_operacion
    #obtener y convertir el valor  de la entrada
    num1=float(entrada1.get())
    #borrar entrada para ingresar num2
    entrada1.delete(0,tk.END)
    #guardar el valor obtenido de entrada en variable var_num1 para hacer uso del valor igual 
    var_num1=num1
    #guardar el valor obtenido de entrada en variable var_operacion para hacer uso del valor igual 
    var_operacion=3 
    #cambiar propiedad de entrada a lectura
    entrada1.config(state="readonly")

def divicion():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #llamar las variables globales 
    global var_num1
    global var_operacion
    #obtener y convertir el valor  de la entrada
    num1=float(entrada1.get())
    #borrar entrada para ingresar num2
    entrada1.delete(0,tk.END)
    #guardar el valor obtenido de entrada en variable var_num1 para hacer uso del valor igual 
    var_num1=num1
    #guardar el valor obtenido de entrada en variable var_operacion para hacer uso del valor igual 
    var_operacion=4
    #cambiar propiedad de entrada a lectura 
    entrada1.config(state="readonly")

def porcentaje():
    #habilitar la entrada a normal
    entrada1.config(state="normal")
    #llamar las variables globales 
    global var_num1
    global var_operacion
    #obtener y convertir el valor  de la entrada
    num1=float(entrada1.get())
    #borrar entrada para ingresar num2
    entrada1.delete(0,tk.END)
    #guardar el valor obtenido de entrada en variable var_num1 para hacer uso del valor igual 
    var_num1=num1
    #guardar el valor obtenido de entrada en variable var_operacion para hacer uso del valor igual 
    var_operacion=5
    #cambiar propiedad de entrada a lectura
    entrada1.config(state="readonly")

def limpiar():
    #cambiar propiedad de entrada a normal
    entrada1.config(state="normal")
    #limpiar ebtrada
    entrada1.delete(0,tk.END)
    #inicializar las variables globales a 0 para evitarproblemas logicos 
    global var_num1
    global var_operacion
    var_num1=0
    var_operacion=0
    #cambiar propiedad de entrada lectura
    entrada1.config(state="readonly")



def igual():
    try:
        #cambiar propiedad de entrada a normal
        entrada1.config(state="normal")
        #mandamos a llamar las variables globales para el uso 
        global var_num1
        global var_operacion
        #obtener el numero dos y combertirlo a float
        num2=float(entrada1.get())
        #borrar entrada para depues mandar el resultado
        entrada1.delete(0,tk.END)
        #empezamos validacion de var_operacion por que contiene la operacion 
        #seleccionda
        if var_operacion==1:
            sum=var_num1+num2
            entrada1.insert(0,sum)
        elif var_operacion==2:
            res=var_num1-num2
            entrada1.insert(0,res)
        elif var_operacion==3:
            mult=var_num1*num2
            entrada1.insert(0,mult)
        elif var_operacion==4:
            divi=var_num1/num2
            entrada1.insert(0,divi)
        elif var_operacion==5:
            porce=(var_num1/100)*num2
            entrada1.insert(0,porce)
    except ZeroDivisionError:
        messagebox.showerror("Error", "No puedes dividir entre cero")


#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("Ejercicio 9")
#definir tamaño de ventana 
ventana_principal.geometry("300x300")

#centramos la ventana en la pantalla 
#obtener el ancho del monitor con propiedad winfo
window_width=ventana_principal.winfo_screenwidth()
#obtener el alto de monitor propiedad winfo
window_height=ventana_principal.winfo_screenheight()
#a partir del ancho de la pantalla obtener las coordenadas totales del monitor 
x_coordinante=int((window_width /2)-(300/2))
#a partir del alto de la pantalla obtener las coordenadas totales del monitor 
y_coordinante=int((window_height /2)-(300/2))
#a partir de las coordenadas x/y obtener el eje central y ubicamos la ventana al centro 
ventana_principal.geometry(f"300x300+{x_coordinante}+{y_coordinante}")

#crear la barra de Menu
barra_principal=tk.Menu(ventana_principal)

#----Submenu opciones-----
#definimoa submenu dentro de menu principal 
menu_opciones=tk.Menu(barra_principal,tearoff=0)
menu_opciones.add_command(label="Nuevo")
menu_opciones.add_command(label="Abriri")
menu_opciones.add_separator()

#asignamos una funcion a la opcion salir 
menu_opciones.add_command(label="salir",command=salir)

#------Submenu tamaño-----
menu_saize=tk.Menu(barra_principal,tearoff=1)
menu_saize.add_command(label="300x200",command=pantalla_s)
menu_saize.add_command(label="600x400",command=pantalla_m)
menu_saize.add_command(label="1020x800",command=pantalla_g)

#--------Agregamos de submenu a barra principal
#agregar el menu opciones a la barra principal
barra_principal.add_cascade(label="opciones",menu=menu_opciones)
barra_principal.add_cascade(label="tamaño",menu=menu_saize)
ventana_principal.config(menu=barra_principal)

#----componetntes
entrada1=tk.Entry(ventana_principal,width=40, justify="right",state="readonly")
entrada1.grid(row=0, column=0)


#Botones
botones=tk.Button(ventana_principal,text="7",widt=2, height=2,command=siete)
botones.grid(row=1, column=0)
botones0_text2=tk.Button(ventana_principal,text="8",widt=2, height=2,command=ocho)
botones0_text2.grid(row=1, column=1)

botones1=tk.Button(ventana_principal,text="9",widt=2, height=2,command=nueve)
botones1.grid(row=1, column=2)
botones2=tk.Button(ventana_principal,text="4",widt=2, height=2,command=cuatro)
botones2.grid(row=2, column=0)

botones3=tk.Button(ventana_principal,text="5",widt=2, height=2,command=cinco)
botones3.grid(row=2, column=1)
botones4=tk.Button(ventana_principal,text="6",widt=2, height=2,command=seis)
botones4.grid(row=2, column=2)
botones5=tk.Button(ventana_principal,text="1",widt=2, height=2,command=uno)
botones5.grid(row=3, column=0)
botones6=tk.Button(ventana_principal,text="2",widt=2, height=2,command=dos)
botones6.grid(row=3, column=1 )

botones7=tk.Button(ventana_principal,text="3",widt=2, height=2,command=tres)
botones7.grid(row=3, column=2)
botones8=tk.Button(ventana_principal,text="C",widt=2, height=2,command=limpiar)
botones8.grid(row=4, column=0)

botones9=tk.Button(ventana_principal,text="0",widt=2, height=2,command=cero)
botones9.grid(row=4, column=1)
botones10=tk.Button(ventana_principal,text=".",widt=2, height=2,command=punto)
botones10.grid(row=4, column=2)

botones11=tk.Button(ventana_principal,text="+",widt=2, height=2,command=suma)
botones11.grid(row=1, column=3)
botones12=tk.Button(ventana_principal,text="/",widt=2, height=2,command=divicion)
botones12.grid(row=1, column=4)

botones13=tk.Button(ventana_principal,text="-",widt=2, height=2,command=resta)
botones13.grid(row=2, column=3)
botones14=tk.Button(ventana_principal,text="%",widt=2, height=2,command=porcentaje)
botones14.grid(row=2, column=4)

botones15=tk.Button(ventana_principal,text="x",widt=2, height=2,command=multiplicacion)
botones15.grid(row=3, column=3)
botones16=tk.Button(ventana_principal,text="=",widt=2, height=2,command=igual)
botones16.grid(row=3, column=4)

ventana_principal.mainloop()



