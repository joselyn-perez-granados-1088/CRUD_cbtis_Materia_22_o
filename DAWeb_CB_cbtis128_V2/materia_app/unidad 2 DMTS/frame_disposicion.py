#importamos libreria
import tkinter as tk
#cremos ventana principal del programa
ventana_principal = tk.Tk()
ventana_principal.title("frame con disposicion de widgets")
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

#creamos frame1 
frame_suparior=tk.Frame(ventana_principal,bg="blue")
frame_suparior.pack(side="top",fill="X")

#creamos frame2
frame_inferiro=tk.Frame(ventana_principal,bg="red")
frame_inferiro.pack(side="bottom",fill="x")

#creamos boton y etiqueta oara frame superiro 
etiquta_sup=tk.Label(frame_suparior,text="etiqueta superior")
etiquta_sup.pack(pady=10)
boton_sup=tk.Button(frame_suparior,text="Boton superior")
boton_sup.pack(pady=10)

#creamos boton y eqtiqueta para frame inferiro 
etiqueta_inf=tk.Label(frame_inferiro,text="etiqueta inferior")
etiqueta_inf.pack(pady=10)
boton_inf=tk.Button(frame_inferiro,text="Boton inferior")
boton_inf.pack(pady=10)

#Mainloop
ventana_principal.mainloop()