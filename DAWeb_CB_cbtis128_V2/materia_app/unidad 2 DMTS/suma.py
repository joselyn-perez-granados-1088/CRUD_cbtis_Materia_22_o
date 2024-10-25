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
    txt1.delete(0, tk.END)
    txt2.delete(0, tk.END)
    etiqueta4.config(text="")

def mostrar():
    try:
        num1=int(txt1.get())
        num2=int(txt2.get())
        resul=num1+num2
        etiqueta4.config(text=resul)
    except ValueError:
        messagebox.showwarning("Entrada no valida", "Favor de introducion un  numero valido")

#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("Ejercicio suma")
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

#-----componentes 
etiqueta1=tk.Label(ventana_principal, text="ingresa el primer numero")
etiqueta1.pack()
txt1=tk.Entry(ventana_principal)
txt1.pack(pady=5)
etiqueta2=tk.Label(ventana_principal, text="ingresa el segundo numero")
etiqueta2.pack()
txt2=tk.Entry(ventana_principal)
txt2.pack(pady=5)
etiqueta3=tk.Label(ventana_principal,text="Resultado es:")
etiqueta3.pack(pady=5)
etiqueta4=tk.Label(ventana_principal, text="")
etiqueta4.pack(pady=5)
#boton mostrar 
boton1=tk.Button(ventana_principal, text="Mostrar resultado",command=mostrar)
boton1.pack(pady=5)

boton2=tk.Button(ventana_principal,text="Limpiar campos",command=limpiar)
boton2.pack(pady=5)

ventana_principal.mainloop()