#importar libreria tkinter 
import tkinter as tk 
#definimos ventana princioal
ventana_principal=tk.Tk()
ventana_principal.title("Freame Grid")

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


#definimos el frame 
frame=tk.Frame(ventana_principal)
#definimos el tipo de diseño para el frame 
frame.grid()

#----Etiquetas y botones 
label1=tk.Label(frame,text="Fila 0, columna 0").grid(row=0, coliumn=0)
label2=tk.Label(frame,text="Fila 0, columna 1").grid(rox=0, column=1)
label3=tk.Label(frame,text="fila 1, columna 0").grid(row=1, column=0)
label4=tk.Label(frame,text="fila 1, columna 1").grid(row=1, column=1)
boton1=tk.Button(frame,text="fila 2, columna 0").grid(row=2,column=0)
boton2=tk.Button(frame,text="fila 2, columna 1").grid(row=2, column=1)

ventana_principal.mainloop()