import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
#--------variable global
#son variables globales por que en caso de requerirlas las mandamos a llamar
#las variables tienen que ser decalradas e iniciadas
var_saldo=0

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

def ventana_secundaria():
    global entrada1
    global entrada2
    #decalrar la ventana secundaria con toplevel
    ventana_secundaria=tk.Toplevel(ventana_principal)
    #establecemos el titulo a la ventana secuandaira
    ventana_secundaria.title("ventana secuandaria")
    #definimos la dimencion de la ventana secuandaira
    ventana_secundaria.geometry("300x200")
    etiqueta1=tk.Label(ventana_secundaria, text="ingrese monto")
    
    #empaquetar la etiqueta para empezar la ventana
    etiqueta1.grid()
    entrada1=tk.Entry(ventana_secundaria,width=20, justify="right")
    entrada1.grid(row=2, column=0)
    
    etiqueta2=tk.Label(ventana_secundaria, text="ingrese N. cuenta")
    etiqueta2.grid(row=3, column=0)
    entrada2=tk.Entry(ventana_secundaria,width=20, justify="right")
    entrada2.grid(row=4, column=0)
    
    #boton limpiar
    boton1=tk.Button(ventana_secundaria,text="Aceptar",command=Aceptar)
    boton1.grid(row=5,column=0)
    #boton limpiar
    boton2=tk.Button(ventana_secundaria, text="cancelar",command=cancelar_ventana_secuandaria_destroy)
    boton2.grid(row=5,column=1)
    #decalramos boton para  mandar a llamar ventana secucndaria 

def Aceptar():
        global var_saldo
        global entrada1
        global entrada2
        global etiqueta3
        
        Tran=float(entrada1.get())

        messagebox.showinfo("Treanferencia Exitosa",f"Trasferiste: {Tran}")

def Transferir():
        global ventana_secundaria 
        global var_saldo 
        etiqueta2.config(text=f"saldo:{var_saldo}")
        ventana_secundaria()

def cancelar_ventana_secuandaria_destroy ():
     global ventana_secundaria
     if ventana_secundaria is not None:
          ventana_secundaria.destroy()
          









def limpiar():
    #cambiar propiedad de entrada a normal
    entrada1.config(state="normal")
    #limpiar ebtrada
    entrada1.delete(0,tk.END)
    #inicializar las variables globales a 0 para evitarproblemas logicos 
    global var_saldo
    var_saldo=0
    #cambiar propiedad de entrada lectura
    entrada1.config(state="readonly")
    
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

def Abonar():

        #cambiar propiedad de entrada a normal
        entrada1.config(state="normal")
        #mandamos a llamar las variables globales para el uso 
        global var_saldo
        #obtener el numero dos y combertirlo a float
        num1=float(entrada1.get())
        opc=var_saldo+num1
        var_saldo=opc
        #borrar entrada para depues mandar el resultado
        entrada1.delete(0,tk.END)
        #empezamos validacion de var_operacion por que contiene la operacion
        etiqueta3.config(text=var_saldo)
        messagebox.showinfo(f"transferancia",f"Abono exitoso")

def  Retirar():
        #cambiar propiedad de entrada a normal
        entrada1.config(state="normal")
        #mandamos a llamar las variables globales para el uso 
        global var_saldo
        #obtener el numero dos y combertirlo a float
        num1=float(entrada1.get())
        opc=var_saldo-num1
        var_saldo=opc
        #borrar entrada para depues mandar el resultado
        entrada1.delete(0,tk.END)
        #empezamos validacion de var_operacion por que contiene la operacion
        etiqueta3.config(text=var_saldo)
        messagebox.showinfo(f"transferancia",f"HAS RETIRADO TU DINERO")







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

#----componetntes}

etiqueta1=tk.Label(ventana_principal,text="cagero automatico" )
etiqueta1.grid(row=0,column=0)

etiqueta2=tk.Label(ventana_principal,text="Saldo:$" )
etiqueta2.grid(row=1,column=0)

etiqueta3=tk.Label(ventana_principal,text="" )
etiqueta3.grid(row=1,column=1)

entrada1=tk.Entry(ventana_principal,width=20, justify="right",state="readonly")
entrada1.grid(row=2, column=0)


#Botones
botones=tk.Button(ventana_principal,text="7",widt=2, height=2,command=siete)
botones.grid(row=3, column=0)
botones0_text2=tk.Button(ventana_principal,text="8",widt=2,height=2,command=ocho)
botones0_text2.grid(row=3, column=1)

botones1=tk.Button(ventana_principal,text="9",widt=2, height=2,command=nueve)
botones1.grid(row=3, column=2)
botones2=tk.Button(ventana_principal,text="4",widt=2, height=2,command=cuatro)
botones2.grid(row=4, column=0)

botones3=tk.Button(ventana_principal,text="5",widt=2, height=2,command=cinco)
botones3.grid(row=4, column=1)
botones4=tk.Button(ventana_principal,text="6",widt=2, height=2,command=seis)
botones4.grid(row=4, column=2)

botones5=tk.Button(ventana_principal,text="1",widt=2, height=2,command=uno)
botones5.grid(row=5, column=0)
botones6=tk.Button(ventana_principal,text="2",widt=2, height=2,command=dos)
botones6.grid(row=5, column=1 )


botones7=tk.Button(ventana_principal,text="3",widt=2, height=2,command=tres)
botones7.grid(row=5, column=2)

botones9=tk.Button(ventana_principal,text="0",widt=2, height=2,command=cero)
botones9.grid(row=6, column=1)
botones10=tk.Button(ventana_principal,text=".",widt=2, height=2,command=punto)
botones10.grid(row=6, column=2)

botones11=tk.Button(ventana_principal,text="Abonar",widt=5, height=2,command=Abonar)
botones11.grid(row=3, column=3)
botones12=tk.Button(ventana_principal,text="Retirar",widt=5, height=2,command=Retirar)
botones12.grid(row=4, column=3)

#decalramos boton para  mandar a llamar ventana secucndaria 
boton13= tk.Button(ventana_principal,text="Tranferir",widt=6, height=2,command=Transferir)
boton13.grid(row=5, column=3)


botones14=tk.Button(ventana_principal,text="Limpiar",widt=5, height=2,command=limpiar)
botones14.grid(row=6, column=3)



ventana_principal.mainloop()



