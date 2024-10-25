#importar libreria 
import tkinter as tk

#definimos ventana principal 
ventana_principal=tk.Tk()
ventana_principal.title("frame scrollbar")

#definimos canva en ventana principal 
canvas=tk.Canvas(ventana_principal,width=300,height=200)
canvas.pack(side="left")

#definimos scrollbar
scrollbar=tk.Scrollbar(ventana_principal,orient="vertical",command=canvas.yview)
scrollbar.pack(side="right",fill="y")

#configuracion de canva
canvas.config(yscrollcommand=scrollbar.set)

#decalracion de frame que contendra el widgeth canva 
frame=tk.Frame(canvas)

#añadimos contenido al frame 20 etiquetas 
for i in range(20):
    tk.Label(frame,text="etiqueta"+str(i)).pack()

#creamos el rendrizdor del canvas dentro del frame 
canvas.create_window((0,0), window=frame, anchor="nw")

#se realizara las actualizaciones frecuentes para que aparezca el 
#canva dentro del frame 
frame.update_idletasks()

#ajustamos tamaño del scroll
canvas.config(scrollregion=canvas.bbox("all"))


ventana_principal.mainloop()


