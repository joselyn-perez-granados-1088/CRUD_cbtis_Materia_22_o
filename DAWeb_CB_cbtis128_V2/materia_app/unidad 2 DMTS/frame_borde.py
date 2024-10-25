#importamos libreria tkinte 


import tkinter as tk
#cremos ventana principal del programa
ventana_principal = tk.Tk()
ventana_principal.title("frame con borde")
#tipos de bordes
#raides
#sunken
#groove
#ridge
#flat
frame=tk.Frame(ventana_principal,bg="gray",relief="flat",bd=5)
frame.pack(pady=10)

#creamos etiqueta dentro del 
etiqueta=tk.Label(frame,text="estiqueta dentro del frame")
etiqueta.pack(pady=10)

boton=tk.Button(frame,text="Boton dentro de frame")
boton.pack(pady=10)


ventana_principal.mainloop()