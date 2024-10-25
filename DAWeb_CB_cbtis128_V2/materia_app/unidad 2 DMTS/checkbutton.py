#importe de libreria
import tkinter as tk 
#---funcion 
def mostrar_seleccion():
    #guaradar seleccion en una lista
    opcion_seleccionada=[]
    if var1.get()== 1:
        opcion_seleccionada.append("opcion 1")
    if var2.get()== 1:
        opcion_seleccionada.append("opcion 2")
    if var3.get()==1:
        opcion_seleccionada.append("opcion 3")

    etiqueta.config(text=f"selecciono:{','.join(opcion_seleccionada)}")

#decalramos la ventana principal 
ventana_principal=tk.Tk()
ventana_principal.title("Chechchbutton")

#Definir tamaño de ventana
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

#-------componentes 
#decalrar variable para los checkbutton 
var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()

#decalar checkcbutton 
cb1=tk.Checkbutton(ventana_principal, text="opcion 1", variable=var1)
cb1.pack()
cb2=tk.Checkbutton(ventana_principal,text="opcion 2",variable=var2)
cb2.pack()
cb3=tk.Checkbutton(ventana_principal,text="opcion 3",variable=var3)
cb3.pack()

#boton 
boton=tk.Button(ventana_principal, text="mostrar seleccion",command=mostrar_seleccion)
boton.pack()
#etiqueta
etiqueta=tk.Label(ventana_principal, text="")
etiqueta.pack()

ventana_principal.mainloop()