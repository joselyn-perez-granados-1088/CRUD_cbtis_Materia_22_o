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

def habilita_area():
    if var1.get()==1:
        entrada_base.config(state="normal")
    else:
        entrada_base.config(state="disabled")
    if var1.get()==1:
        entrada_altura.config(state="normal")
    else:
        entrada_altura.config(state="disabled")

def habiliar_perimetro():
    if var1.get()==1:
        entrada_lado.config(state="normal")
    else:
        entrada_lado.config(state="disabled")

def limpiar():
    cb1.current(0)
    entrada_altura.delete(0,tk.END)
    entrada_base.delete(0,tk.END)
    entrada_lado.delete(0,tk.END)

def resultado():
    try:
        opcion_seleccionada=cb1.get()
    
        if opcion_seleccionada=="Area":
            base=entrada_base.get()
            altura=entrada_altura.get()
            area=(base*altura)/2
            etiqueta7.config(text=f"El area es: {area:.2f}")
        elif opcion_seleccionada=="Perimetro":
            lado=float(entrada_lado.get())
            perimetro=lado+lado+lado
            etiqueta7.config(text=f"El perimetro es:{perimetro:.2f}")
    except ValueError:
        messagebox.showwarning("Error","Favor de ingresar valor valido")



#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("ejercicio 4")
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



#---------componentes 
#etiqueta1
etiqueta1=tk.Label(ventana_principal,text="por favor selecciones una opcion ")
etiqueta1.grid(row=0, column=1, padx=5, pady=5)

opciones=["Seleciona una opcion","Area","Perimetro"]
cb1=ttk.Combobox(ventana_principal, values=opciones)
cb1.grid(row=1, column=1, padx=5, pady=5)
cb1.current(0)

#etiqueta 
etiqueta2=tk.Label(ventana_principal, text="decaurdo a tu seleccion desmarca")
etiqueta2.grid(row=3, column=1,padx=5, pady=5)

var1=tk.IntVar()
check_area=tk.Checkbutton(ventana_principal, text="Area", variable=var1,command=habilita_area)
check_area.grid(row=4, column=0, padx=5, pady=5)
var2=tk.IntVar()
check_perimetro=tk.Checkbutton(ventana_principal, text="Perimetro", variable=var2,command=habiliar_perimetro)
check_perimetro.grid(row=4, column=2, padx=5, pady=5)

#etiqueta 
etiqueta3=tk.Label(ventana_principal, text="Base")
etiqueta3.grid(row=5, column=0,padx=5, pady=5)
etiqueta4=tk.Label(ventana_principal, text="Lado")
etiqueta4.grid(row=5, column=2,padx=5, pady=5)

#entry 
entrada_base=tk.Entry(ventana_principal,state="disabled")
entrada_base.grid(row=6, column=0,padx=5, pady=5)
entrada_lado=tk.Entry(ventana_principal, state="disabled")
entrada_lado.grid(row=6, column=2,padx=5, pady=5)

#etiqueta 
etiqueta5=tk.Label(ventana_principal,text="Altura")
etiqueta5.grid(row=7, column=0,padx=5, pady=5)

entrada_altura=tk.Entry(ventana_principal,state="disabled")
entrada_altura.grid(row=8, column=0,padx=5, pady=5)


#etiqueta resultado 
etiqueta6=tk.Label(ventana_principal,text="resultado es:")
etiqueta6.grid(row=8, column=1,padx=5, pady=5)
etiqueta7=tk.Label(ventana_principal,text="")
etiqueta7.grid(row=9, column=1,padx=5, pady=5)

#Botones 
botones_resultado=tk.Button(ventana_principal,text="resultado",command=resultado)
botones_resultado.grid(row=10, column=0,padx=5, pady=5)
botones_limpiar=tk.Button(ventana_principal,text="limpiar",command=limpiar)
botones_limpiar.grid(row=10, column=2,padx=5, pady=5)

ventana_principal.mainloop()