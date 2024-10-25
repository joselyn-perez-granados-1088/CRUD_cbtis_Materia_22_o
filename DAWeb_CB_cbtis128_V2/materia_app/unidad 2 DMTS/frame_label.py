#importe libreria tkinter 
import tkinter as tk 
#definimos ventana principal 
ventana_principal=tk.Tk()
ventana_principal.title("frame label")

#definimos la dimencion de ventana principal
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

#definimos frame label 
labelframe=tk.LabelFrame(ventana_principal,text="grupo de botones")
labelframe.pack(padx=10, pady=10)

#botones 
#definimos botones 
boton1=tk.Button(labelframe,text="Boton 1")
boton1.pack(padx=10,pady=10)

boton2=tk.Button(labelframe,text="Boton 2")
boton2.pack(padx=10, pady=10)

ventana_principal.mainloop()