import tkinter as tk 
from tkinter import messagebox
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
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta4.config(text="")

def resultado():
    #otener el radioboton seleccionado y se guard en variable 
    try:
        radio_seleccion= var.gey()
        #Obtendo lo que se escribira en campo de texto y convierto a entero
        num1=int(entrada1.get())
        num2=int(entrada2.get())
        #realizar operaciones de acuerdo al radioboton seleccionado
        if radio_seleccion==" suma":
            suma=num1+num2
            etiqueta4.config(text=suma)
        elif radio_seleccion==" resta":
            resta=num1-num2
            etiqueta4.config(text=resta)
        if radio_seleccion==" multiplicacion":
            multi=num1*num2
            etiqueta4.config(text=multi)
        if radio_seleccion=="divicion":
            divicion=num1/num2
            etiqueta4.config(text=divicion)
    except ValueError:
        messagebox.showwarning("Error","Ingrese un numero valido")

def mostrar_seleccion():
    #declaramos vaariable para obtener la informacion de variable var
    seleccion=var.get()
    #asignamos texto a la etiqueta con la variable seleccion
    etiqueta.config(text=f"Has seleccionado:{seleccion}")


#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("Ejercicio 1 UII")
#definir tamaño de ventana 
ventana_principal.geometry("300x400")

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
ventana_principal.geometry(f"300x400+{x_coordinante}+{y_coordinante}")

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

#-----componentes 
# Etiqueta 
etiqueta1=tk.Label(ventana_principal, text="ingresa el primer numero")
etiqueta1.pack()
#entry
entrada1=tk.Entry(ventana_principal)
entrada1.pack(pady=5)
#etiqueta 2
etiqueta2=tk.Label(ventana_principal, text="ingresa el segundo numero")
etiqueta2.pack()
#entry
entrada2=tk.Entry(ventana_principal)
entrada2.pack(pady=5)
#etiqueta 3
etiqueta3=tk.Label(ventana_principal,text="Resultado es:")
etiqueta3.pack(pady=5)
#etiqueta 4
etiqueta4=tk.Label(ventana_principal, text="")
etiqueta4.pack(pady=5)

#-----Radiobuton 
#creae variable que almacenar el valor seleccionado 
var=tk.StringVar()

radio1=tk.Radiobutton(ventana_principal,text=" suma", variable=var, value=" suma").pack()
radio2=tk.Radiobutton(ventana_principal, text=" resta", variable=var, value=" resta").pack()
radio3=tk.Radiobutton(ventana_principal, text=" multiplicacion", variable=var, value=" multiplicacion").pack()
radio4=tk.Radiobutton(ventana_principal, text=" divicion", variable=var, value=" divicion").pack()

#valor por default de varaible para almacenar valores 
var.set(" suma")

#boton mostrar 
boton1=tk.Button(ventana_principal, text="Mostrar resultado",command=resultado)
boton1.pack()

#boton mostrar 
boton2=tk.Button(ventana_principal, text="limpiar",command=resultado)
boton2.pack()

#etiqueta 
etiqueta=tk.Label(ventana_principal, text="")
etiqueta.pack()


ventana_principal.mainloop()