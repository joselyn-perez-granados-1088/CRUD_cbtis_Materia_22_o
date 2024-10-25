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

def habilitar_entry(event):
    opcion_comcocox=cb1.get() 
    if opcion_comcocox=="USA" or opcion_comcocox=="MX" or opcion_comcocox=="EU":
        cb1.config(state="normal")
    else:
        cb2.config(state="disabled")


def limpiar():
    #limpiamos entrada
    entrada_dinero.delete(0,tk.END)
    #limpimos combobox
    cb1.current(0)
    cb2.current(0)
    #desabilitar conbobox
    cb1.config(state="disabled")

def convertir():
    try:
        #obtenemos el valor de entry y los convertimos a entero
        monton=float(entrada_dinero.get())
        
        #obtenemos lo que se obtiene del combobox
        opcion_seleccionada1=cb1.get()
        opcion_seleccionada2=cb2.get()
        
        if opcion_seleccionada1==opcion_seleccionada2:
            etiqueta4.config(test=f"iguales")
        elif opcion_seleccionada1=="MX" and opcion_seleccionada2=="USA":
            resultado=monton/18
            messagebox.showwarning("la convercion es:",resultado)
        
        elif opcion_seleccionada1=="MX" and opcion_seleccionada2=="EU":
                resultado=monton/21
                messagebox.showwarning("la convercion es:",resultado)
        elif opcion_seleccionada1=="USA" and opcion_seleccionada2=="EU":
                resultado=monton/.90
                messagebox.showwarning("la convercion es:",resultado)
        elif opcion_seleccionada1=="EU" and opcion_seleccionada2=="USA":
                resultado=monton/1.10
                messagebox.showwarning("la convercion es:",resultado)
        elif opcion_seleccionada1=="EU" and opcion_seleccionada2=="MX":
                resultado=monton*21
                messagebox.showwarning("la convercion es:",resultado)
        elif opcion_seleccionada1=="USA" and opcion_seleccionada2=="MX":
                resultado=monton*18
                messagebox.showwarning("la convercion es:",resultado)
        
    except ValueError:
        messagebox.showwarning("error","ingrese valor valido")

#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("ejercicio 5")
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


#---------componentes 
#etiqueta1
etiqueta1=tk.Label(ventana_principal,text="Ingresa el monto a convertir: ")
etiqueta1.pack()

#entry 
entrada_dinero=tk.Entry(ventana_principal)
entrada_dinero.pack()

#etiqueta 2
etiqueta2=tk.Label(ventana_principal, text="Seleciona la moneda a principal:")
etiqueta2.pack()

#opciones 1
opcion=["Seleciona la moneda a principal","MX","USA","EU"]
cb1=ttk.Combobox(ventana_principal, values=opcion)
cb1.pack()
#establecer la opcion determinada 
cb1.current(0)
#etiqueta 3
etiqueta3=tk.Label(ventana_principal, text="Seleciona la moneda a convertir:")
etiqueta3.pack()

cb2=ttk.Combobox(ventana_principal, values=opcion)
cb2.pack()
cb2.current(0)

etiqueta4=tk.Label(ventana_principal, text="")
etiqueta4.pack()
#llamar la fumcion  seleccionar
cb1.bind("<<ComboboxSelected>>",habilitar_entry)

#Botones 
botones_convertir=tk.Button(ventana_principal,text="convertir",command=convertir)
botones_convertir.pack(side="left",fill="x",expand="true")
botones_limpiar=tk.Button(ventana_principal,text="limpiar",command=limpiar)
botones_limpiar.pack(side="left",fill="x",expand="true")


ventana_principal.mainloop()

