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

def habilita_entry(event):
    #obtener lo seleccionado 
    lista_selecciona=cd.get()
    #validar la opcion seleccionada paramhabilitar radiobotones 
    #opcion 1, utilizar el operador no igual diferente ya que la opcion selecionada 
    #al iniciar es igual a vacio(**):
    #opcion2, ess convertir los que se ontiene del combobox a entero 
    #y realizar la validacion de que este entre el 1 al 100
    #if lista_seleccionada !=""
    if lista_selecciona >="":
        radio1.config(state="normal")
        radio2.config(state="normal")
        radio3.config(state="normal")
    else:
        radio1.config(state="disabled")
        radio2.config(state="disabled")
        radio3.config(state="disabled")

def limpiar():
    #limpiamos entrada
    cd.delete(0,tk.END)
    radio1.config(state="disabled")
    radio2.config(state="disabled")
    radio3.config(state="disabled")
    cd.current(0)
    var.set("centimetros")
    var.set("metros")
    var.set("kilometros")

def convertir():
    try:
        #guardar una variable a los que se selecciono de combobox
        lista_seleccionada=int(cd.get())
        radioboton_seleccionada=var.get()
        if radioboton_seleccionada=="centimetros":
            convercion=lista_seleccionada/10
            messagebox.showinfo("centimetros",f"los centimetros son: {convercion}")
        elif radioboton_seleccionada=="metros":
            convercion=lista_seleccionada/100
            messagebox.showinfo("metros",f"Los metros son: {convercion}")
        elif radioboton_seleccionada=="Kilometros":
            convercion=lista_seleccionada/1000000
            messagebox.showinfo("kilometros",f"Los metros son: {convercion}")
    except TypeError:
        messagebox.showerror("Error","Los tipos de datos no coinciden")


#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("Ejercicio 6")
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


#---------componentes 

#etiqueta1
etiqueta1=tk.Label(ventana_principal,text="Selecciona una opcion del 1 al 20: ")
etiqueta1.pack()
#creamos una lista
lista=[]
#hacemos una funcion for para llamar
for i in range(1,21):
    lista.append(i)
cd=ttk.Combobox(ventana_principal,values=lista)
cd.pack()
#establecer la opcion determinada 
cd.current(0)
#llamar la fumcion  seleccionar
cd.bind("<<ComboboxSelected>>",habilita_entry)

#etiqueta2
etiqueta2=tk.Label(ventana_principal,text="Selecciona una longitud: ")
etiqueta2.pack()

#-----Radiobuton 
#creae variable que almacenar el valor seleccionado 
var=tk.StringVar()

radio1=tk.Radiobutton(ventana_principal,text="centimetros", variable=var, value="centimetros",state="disabled")
radio1.pack()
radio2=tk.Radiobutton(ventana_principal, text="metros", variable=var, value="metros",state="disabled")
radio2.pack()
radio3=tk.Radiobutton(ventana_principal, text="kilometros", variable=var, value="kilometros",state="disabled")
radio3.pack()

#valor por default de varaible para almacenar valores 
var.set("centietros")


etiqueta4=tk.Label(ventana_principal, text="")
etiqueta4.pack()
#Botones 
botones_convertir=tk.Button(ventana_principal,text="convertir",command=convertir)
botones_convertir.pack(side="left",fill="x",expand="true")
botones_limpiar=tk.Button(ventana_principal,text="limpiar",command=limpiar)
botones_limpiar.pack(side="left",fill="x",expand="true")




ventana_principal.mainloop()