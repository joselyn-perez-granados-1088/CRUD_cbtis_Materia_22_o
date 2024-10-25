#conboBox 
#libreria de entrada 
import tkinter  as tk 
from tkinter import messagebox
#usar libreria para el menejo del conbobox
from tkinter import ttk 
#decalramos math
import math
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
    #limpiar entrada
    entrada2.delete(0, tk.END)
    #limpiar etiqueta de resultado
    etiqueta4.config(text="")
    #seteamos a primera opcion combobox
    Combobox.current(0)
    entrada2.config(state="disabled")

def habilitar_entry(event):
    opcion_combobox=Combobox.get()
    #habiliatar el entry si se selecciono area o perimetro
    if opcion_combobox=="Area" or Combobox.get()=="Perimetro":
        entrada2.config(state="normal")
    else:
        entrada2.config(state="disabled")


def resultado():
    try: 
        opcion_combobox=Combobox.get()
        radio=int(entrada2.get())
    #realizar operaciones de acuerdo al radioboton seleccionado
        if opcion_combobox=="Area":
            area= math.pi*(radio**2)
            etiqueta4.config(text=area)
        
        elif opcion_combobox==" Perimetro":
            perimetro= (2* math.pi)*radio
            etiqueta4.config(text=perimetro)
        
        
    except ValueError:
        messagebox.showwarning("Error","Ingrese un numero valido")




def mostrar_seleccion():
    seleccion=Combobox.get()
    etiqueta2.config(text=f"has seleccionado: {seleccion}")
#creamos ventana principal 
ventana_principal=tk.Tk()
#
ventana_principal.title("ConboBox")

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

#componentes 
etiqueta1=tk.Label(ventana_principal,text="Por favor selecciona una opcion:")
etiqueta1.pack()

#------combobox 

#crear lista de datos 
opciones=["Selecciona un opcion","Area","Perimetro"]

#decalrar conbobo 
Combobox= ttk.Combobox(ventana_principal, values=opciones)
Combobox.pack()

#Establecer la opcion predeterminada
Combobox.current(0)
Combobox.bind("<<ComboboxSelected>>",habilitar_entry)
#Etiqueta 
etiqueta2=tk.Label(ventana_principal, text="ingresa el radio")
etiqueta2.pack(pady=5)

#entry
entrada2=tk.Entry(ventana_principal,state="disabled")
entrada2.pack(pady=5)

#etiquetas
etiqueta3=tk.Label(ventana_principal,text="Resultado es:")
etiqueta3.pack()
etiqueta4=tk.Label(ventana_principal, text="")
etiqueta4.pack()

#boton resultado
boton_resultado=tk.Button(ventana_principal, text="Mostrar resultado",command=resultado)
boton_resultado.pack(side="left",padx=40)


#boton limpiar
boton_limpiar=tk.Button(ventana_principal, text="limpiar",command=limpiar)
boton_limpiar.pack(side="right",padx=40)



ventana_principal.mainloop()