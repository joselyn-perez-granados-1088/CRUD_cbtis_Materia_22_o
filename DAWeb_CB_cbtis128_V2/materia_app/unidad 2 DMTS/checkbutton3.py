#importe de libreria
import tkinter as tk 
#---funcion 
def mostrar_seleccion():
    if var1.get()==1:
        boton.config(state="normal")
    else:
        boton.config(state="disabled")



#decalramos la ventana principal 
ventana_principal=tk.Tk()
ventana_principal.title("Chechchbutton3")

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


#decalar checkcbutton 
cb1=tk.Checkbutton(ventana_principal, text="activar boton", variable=var1,command=mostrar_seleccion)
cb1.pack()


#boton 
boton=tk.Button(ventana_principal, text="mostrar seleccion",state="disabled")
boton.pack()

ventana_principal.mainloop()