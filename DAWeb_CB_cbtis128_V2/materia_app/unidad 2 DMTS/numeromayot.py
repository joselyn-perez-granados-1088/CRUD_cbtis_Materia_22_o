#importamos libreria 
import tkinter as tk 
from tkinter import messagebox
from tkinter import ttk
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

def limpiar():
    #limpiar spinbox
    sb1.delete(0,tk.END)
    sb1.insert(0,0)
    sb2.delete(0,tk.END)
    sb2.insert(0,0)
    sb3.delete(0,tk.END)
    sb3.insert(0,0)
    #limpiar ckecbuttpn 
    var1.set(0)
    var2.set(0)
    var3.set(0)
    #limpiar etiqueta 6
    etiqueta6.config(text="")

def resultado():
    try:
        #obtener la informacion del spinbox y convertir a entero
        numero1=int(sb1.get())
        numero2=int(sb2.get())
        numero3=int(sb3.get())
        numero=[numero1,numero2,numero3]
        mayor=max(numero)
        menor=min(numero)
        #obtenerr a partir de condiciones logicos el mayor y  menor o igual
        #validar que los numero son iguales
        if numero1== numero2== numero3:
            etiqueta6.config(text="Los numeros son iguales")
        #validar numero 1
        else:
            etiqueta6.config(text=f"el mayor es: {mayor} y el numero menor es: {menor}")
    except NameError:
        messagebox.showwarning("Error","Variable no encontrada")

def habilitar1():
    if var1.get()==1:
        sb1.config(state="normal")
    else:
        sb1.config(state="disabled")

def habilita2():
    if var2.get()==1:
        sb2.config(state="normal")
    else:
        sb2.config(state="disabled")

def habilitar3():
    if var3.get()==1:
        sb3.config(state="normal")
    else:
        sb3.config(state="disabled")






#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("ejercicio 3")
#definir tamaño de ventana 
ventana_principal.geometry("550x300")

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
ventana_principal.geometry(f"550x300+{x_coordinante}+{y_coordinante}")

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

#varuables para ckecbutton 
var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()


#----------componentes 
#etiqueta 
etiqueta1=tk.Label(ventana_principal, text="Favor de habiliatar los spinbox ")
etiqueta1.grid(row=0, column=1,padx=5, pady=5)


#etiqueta 
etiqueta2=tk.Label(ventana_principal, text="Numero 1")
etiqueta2.grid(row=1, column=0,padx=5, pady=5)

#ckeckbutton
cb1=tk.Checkbutton(ventana_principal, text="Marca/Desmarca",variable=var1, command=habilitar1)
cb1.grid(row=2, column=0, padx=5, pady=5)
#spinbox 
sb1=tk.Spinbox(ventana_principal, from_=0 , to=100,state="disabled")
sb1.grid(row=3, column=0, padx=5, pady=5)

#etiqueta 
etiqueta3=tk.Label(ventana_principal, text="Numero 2")
etiqueta3.grid(row=1, column=1,padx=5, pady=5)

#ckeckbutton
cb2=tk.Checkbutton(ventana_principal,text="Marca/Desmarca",variable=var2,command=habilita2)
cb2.grid(row=2, column=1, padx=5, pady=5)
#spinbox 
sb2=tk.Spinbox(ventana_principal, from_=0 , to=100,state="disabled")
sb2.grid(row=3, column=1, padx=5, pady=5)

#etiqueta 
etiqueta4=tk.Label(ventana_principal, text="Numero 3 ")
etiqueta4.grid(row=1, column=2,padx=5, pady=5 )

#ckeckbutton
cb3=tk.Checkbutton(ventana_principal,text="Marca/Desmarca",variable=var3,command=habilitar3)
cb3.grid(row=2, column=2, padx=5, pady=5)
#spinbox 
sb3=tk.Spinbox(ventana_principal, from_=0 , to=100,state="disabled")
sb3.grid(row=3, column=2, padx=5, pady=5)

#etiqueta para resultado 
etiqueta5=tk.Label(ventana_principal,text="Resultado es:")
etiqueta5.grid(row=4,column=1,padx=5,pady=5)


etiqueta6=tk.Label(ventana_principal,text="")
etiqueta6.grid(row=5,column=1,padx=5,pady=5)

#Boton 
boton_resultado=tk.Button(ventana_principal,text="Resultado",command=resultado)
boton_resultado.grid(row=6,column=0,padx=5,pady=5)

boton_limpiar=tk.Button(ventana_principal,text="Limpiar",command=limpiar)
boton_limpiar.grid(row=6,column=2,padx=5,pady=5)

ventana_principal.mainloop()
