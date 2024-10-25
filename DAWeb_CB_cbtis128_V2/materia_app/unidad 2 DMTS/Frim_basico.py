#importamos libreria tkinter 
import tkinter as tk
#cremos ventana principal del programa
ventana_principal = tk.Tk()
ventana_principal.title("frame Basico")
#definimos la dimencion de ventana principal
ventana_principal.geometry("300x200")
# creamos el frame de nuestra aplicacion 
frame=tk.Frame(ventana_principal)
frame.pack(padx=10)

#creamos etiqueta dentro del 
etiqueta=tk.Label(frame,text="estiqueta dentro del frame")
etiqueta.pack(pady=10)

boton=tk.Button(frame,text="Boton dentro de frame")
boton.pack(pady=10)

#Mainloop
ventana_principal.mainloop()