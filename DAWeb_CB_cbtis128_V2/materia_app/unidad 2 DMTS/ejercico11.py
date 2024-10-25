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

def habilitar():
    if var1.get()==1:
        spinbox_milogramos.config(state="normal")
    else:
        spinbox_milogramos.config(state="disabled")
    if var2.get()==1:
        spinbox_gramos.config(state="normal")
    else:
        spinbox_gramos.config(state="disabled")
    if var3.get()==1:
        spinbox_kilogramos.config(state="normal")
    else:
        spinbox_kilogramos.config(state="disabled")

def limpiar():
    spinbox_milogramos.delete(0,tk.END)
    spinbox_gramos.delete(0,tk.END)
    spinbox_kilogramos.delete(0,tk.END)
    spinbox_milogramos.insert(0,"0")
    spinbox_gramos.insert(0,"0")
    spinbox_kilogramos.insert(0,"0")
    var1.set(0)
    var2.set(0)
    var3.set(0)
    spinbox_milogramos.config(state="disabled")
    spinbox_gramos.config(state="disabled")
    spinbox_kilogramos.config(state="disabled")

def convertir():
    try:
        #obtenemos lo que seleccion  obtiene del combobox
        opcion_seleccionada1=(var1.get())
        opcion_seleccionada2=(var2.get())
        opcion_seleccionada3=(var3.get())
        #LAS VARIABLES LAS CONVERTIMOS A FLOTANTES
        miligramos=float(spinbox_milogramos.get())
        gramos=float(spinbox_gramos.get())
        kilogramos=float(spinbox_kilogramos.get())
        #verificare que checbutoon este seleccionado las posibles convinaciones
        #validamos opcion uno y opcion 2
        if opcion_seleccionada1==1 and opcion_seleccionada2==1:
            #PONEMEOS MILIGRAMOS EN  DIFERENTE A IGUAL A CERO Y EL GRAMOS IGUAL Y IGUAL Y IGUAL A CERO
            if miligramos!=0 and gramos==0:
                #POBEMOS NUETRA OPCION A COMVERTIR QUE ES GRAMOS IGUAL A LA OPCION SELECCIONADA QUE ES MILIGRAMOS
                gr=miligramos/1000
                #HABILITAMOS EL SPINBOX DE GRAMOS A NORMAL
                spinbox_gramos.config(state="normal")
                #BORRAMOS ENTRADA PARA PASAR A PONER EL INSERT
                spinbox_gramos.delete(0,tk.END)
                #PONEMOS EL INSERTE ENTRE PARENTESIS DENTREO ALMACENAMOS A CERO COMA LA VARIABLE A CONVERTIR QUE ES GRAMOS
                spinbox_gramos.insert(0,gr)
        if opcion_seleccionada1==1 and opcion_seleccionada3==1:
            if miligramos!=0 and kilogramos==0:
                kg=miligramos/1,000,000
                spinbox_kilogramos.config(state="normal")
                spinbox_kilogramos.delete(0,tk.END)
                spinbox_kilogramos.insert(0,kg)
        if opcion_seleccionada2==1 and opcion_seleccionada1==1:
            if gramos!=0 and miligramos==0:
                mg=gramos*1000
                spinbox_milogramos.config(state="normal")
                spinbox_milogramos.delete(0,tk.END)
                spinbox_milogramos.insert(0,mg)
        if opcion_seleccionada2==1 and opcion_seleccionada3==1:
            if gramos!=0 and kilogramos==0:
                kg=gramos/1000
                spinbox_kilogramos.config(state="normal")
                spinbox_kilogramos.delete(0,tk.END)
                spinbox_kilogramos.insert(0,kg)
        if opcion_seleccionada3==1 and opcion_seleccionada1==1:
            if kilogramos!=0 and miligramos==0:
                mg=kilogramos*1,000,000
                spinbox_milogramos.config(state="normal")
                spinbox_milogramos.delete(0,tk.END)
                spinbox_milogramos.insert(0,mg)
        if opcion_seleccionada3==1 and opcion_seleccionada2==1:
            if kilogramos!=0 and gramos==0:
                gr=kilogramos*1000
                spinbox_gramos.config(state="normal")
                spinbox_gramos.delete(0,tk.END)
                spinbox_gramos.insert(0,gr)
        if opcion_seleccionada1==1 and opcion_seleccionada2==1 and opcion_seleccionada3==1:
            if miligramos!= 0 and gramos ==0 and kilogramos==0:
                gr=miligramos/1000
                kg=miligramos/1,000,000
                spinbox_gramos.delete(0,tk.END)
                spinbox_kilogramos.delete(0,tk.END)
                spinbox_gramos.insert(0,gr)
                spinbox_kilogramos.insert(0,kg)
            if miligramos== 0 and gramos !=0 and kilogramos==0:
                mg=gramos*1000
                kg=gramos/1000
                spinbox_kilogramos.delete(0,tk.END)
                spinbox_kilogramos.insert(0,kg)
                spinbox_milogramos.delete(0,tk.END)
                spinbox_milogramos.insert(0,mg)
            if miligramos== 0 and gramos ==0 and kilogramos!=0:
                mg=kilogramos*1,000,000
                gr=kilogramos*1000
                spinbox_gramos.delete(0,tk.END)
                spinbox_gramos.insert(0,gr)
                spinbox_milogramos.delete(0,tk.END)
                spinbox_milogramos.insert(0,mg)
    except ValueError:
        messagebox.showwarning("error","ingrese valor valido")





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

#etiqueta1 

etiqueta_milogramos=tk.Label(ventana_principal,text="miligramos" )
etiqueta_milogramos.grid(row=0,column=0)

spinbox_milogramos=tk.Spinbox(ventana_principal,from_=0, to=1000,state="disabled")
spinbox_milogramos.grid(row=1,column=0)

etiqueta_gramos=tk.Label(ventana_principal,text="gramos" )
etiqueta_gramos.grid(row=2,column=0)

spinbox_gramos=tk.Spinbox(ventana_principal,from_=0, to=1000,state="disabled")
spinbox_gramos.grid(row=3,column=0)

etiqueta_kilogramos=tk.Label(ventana_principal,text="kilogramos" )
etiqueta_kilogramos.grid(row=4,column=0)

spinbox_kilogramos=tk.Spinbox(ventana_principal,from_=0, to=1000,state="disabled")
spinbox_kilogramos.grid(row=5,column=0)


var1=tk.IntVar()
check_mg=tk.Checkbutton(ventana_principal, text="mg", variable=var1,command=habilitar)
check_mg.grid(row=1, column=1,padx=5, pady=5)
var2=tk.IntVar()
check_gr=tk.Checkbutton(ventana_principal, text="gr", variable=var2,command=habilitar)
check_gr.grid(row=3, column=1,padx=5, pady=5)

var3=tk.IntVar()
check_kg=tk.Checkbutton(ventana_principal, text="kg", variable=var3,command=habilitar)
check_kg.grid(row=5, column=1, padx=5, pady=5)

#Botones 
botones_resultado=tk.Button(ventana_principal,text="convertir", command=convertir)
botones_resultado.grid(row=6,column=3,padx=5, pady=5)
botones_limpiar=tk.Button(ventana_principal,text="limpiar",command=limpiar)
botones_limpiar.grid(row=6, column=4,padx=5, pady=5)


ventana_principal.mainloop()