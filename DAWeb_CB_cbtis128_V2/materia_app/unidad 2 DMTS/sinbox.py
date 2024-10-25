#importamos libreria 
import tkinter as tk 

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

def valor_cambiado():
    print("valor cambiado:",spinbox_funcion.get())


#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("Sinbox")
#definir tamaño de ventana 
ventana_principal.geometry("300x200")

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
ventana_principal.geometry(f"300x200+{x_coordinante}+{y_coordinante}")

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

#-----sinbox
etiqueta1=tk.Label(text="sinbox basico")
etiqueta1.pack()
#decalaramos sinbox con opcion de decalracion en ventana que aparecera, valor inicial y final 
spinbox=tk.Spinbox(ventana_principal,from_=0, to=10)
spinbox.pack()


#spinbox lista de valores 

etiqueta2=tk.Label(text="Spinbox lista de valores")
etiqueta2.pack()

lista_valores=["rojo","verde","azul","amarillo"]
spinbox_lista=tk.Spinbox(ventana_principal, values=lista_valores)
spinbox_lista.pack()


#spinbox funcion
etiqueta3=tk.Label(text="spinbox con funcion")
etiqueta3.pack()
spinbox_funcion=tk.Spinbox(ventana_principal,from_=0, to=10, command=valor_cambiado)
spinbox_funcion.pack()



#spinbox deshabilitado
etiqueta4=tk.Label(text="spinbox deshabilitado")
etiqueta4.pack()
spinbox_deshabilitado=tk.Spinbox(ventana_principal, from_=0, to=10, state="disabled")
spinbox_deshabilitado.pack()


ventana_principal.mainloop()