import tkinter as tk 
from tkinter import ttk
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
    entrada3.delete(0, tk.END)



def suma():
    try:
        entrada3.delete(0,tk.END)
        num1=int(entrada1.get())
        num2=int(entrada2.get())
        resul=num1+num2
        entrada3.insert(0,resul)
    except ValueError:
        messagebox.showwarning("Entrada no valida", "Favor de introducion un  numero valido")


def resta():
    try:
        entrada3.delete(0,tk.END)
        num1=int(entrada1.get())
        num2=int(entrada2.get())
        resul=num1-num2
        entrada3.insert(0,resul)
    except ValueError:
        messagebox.showwarning("Entrada no valida", "Favor de introducion un  numero valido")

def multiplicacion():
    try:
        entrada3.delete(0,tk.END)
        num1=int(entrada1.get())
        num2=int(entrada2.get())
        resul=num1*num2
        entrada3.insert(0,resul)
    except ValueError:
        messagebox.showwarning("Entrada no valida", "Favor de introducion un  numero valido")

def divicion():
    try:
        entrada3.delete(0,tk.END)
        num1=float(entrada1.get())
        num2=float(entrada2.get())
        resul=num1/num2
        entrada3.insert(0,resul)
    except ValueError:
        messagebox.showwarning("Entrada no valida", "Favor de introducion un  numero valido")


#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("Ejercicio 7")
#definir tamaño de ventana 
ventana_principal.geometry("350x300")

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
ventana_principal.geometry(f"350x300+{x_coordinante}+{y_coordinante}")

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

#etiqueta1
etiqueta1=tk.Label(ventana_principal,text="Primer numero: ")
etiqueta1.grid(row=0, column=0, padx=10, pady=10)

#etiqueta1
etiqueta2=tk.Label(ventana_principal,text="segundo numero: ")
etiqueta2.grid(row=1, column=0, padx=10, pady=10)

#etiqueta1
etiqueta3=tk.Label(ventana_principal,text="Resultado: ")
etiqueta3.grid(row=2, column=0, padx=10, pady=10)

#entry2
entrada1=tk.Entry(ventana_principal)
entrada1.grid(row=0, column=1, padx=10, pady=10)

#entry2
entrada2=tk.Entry(ventana_principal)
entrada2.grid(row=1, column=1, padx=10, pady=10)

#entry2
entrada3=tk.Entry(ventana_principal)
entrada3.grid(row=2, column=1, padx=10, pady=10)

#Botones 
botones_convertir=tk.Button(ventana_principal,text="+",command=suma)
botones_convertir.grid(row=4, column=0, padx=10, pady=10)
botones_limpiar=tk.Button(ventana_principal,text="-",command=resta)
botones_limpiar.grid(row=4, column=1, padx=10, pady=10)

botones_convertir=tk.Button(ventana_principal,text="X",command=multiplicacion)
botones_convertir.grid(row=5, column=0, padx=10, pady=10)
botones_limpiar=tk.Button(ventana_principal,text="/",command=divicion)
botones_limpiar.grid(row=5, column=1, padx=10, pady=10)

botones_limpiar=tk.Button(ventana_principal,text="limpiar",command=limpiar)
botones_limpiar.grid(row=6, column=0, padx=10, pady=10)

ventana_principal.mainloop()



