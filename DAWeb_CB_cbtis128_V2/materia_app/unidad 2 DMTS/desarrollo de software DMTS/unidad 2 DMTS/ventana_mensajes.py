#decalracion de ventanas principal con lubreria tkinter 
#imprimir lobreria tkinter 
#mandamos a mandar a llamr la libreria y le asiganamos un nombre 
#al objetivo para utilizarlo en el codugo , llamado tk
import tkinter as tk 
from tkinter import messagebox
#funciones para mensaje informativo 
def ventana_informacion():
    messagebox.showinfo("informacion","este es un mensaje informativo")

#funcion para menaje advertencia
def ventana_adveretencia():
    messagebox.showwarning("adevertencia ","este es un mensaje de advertencia")
#funcion para mensaje error 

#funcion para preguntar si/no 

#funcion para preguntar acempar/cancelar 

#funcion para preguntar si/no/cancelar

#creamos ventana principal 
ventana_principal=tk.Tk()
#establecemos titulo a la ventana principal
ventana_principal.title("ventana principal")
#definimos la dimencion de la ventana principla 
ventana_principal.geometry("300x350")

#-----  Boton mensaje informativo y eqtiqueta
etiqueta_info=tk.Label(ventana_principal,text="preciona para ventana de informacion")
etiqueta_info.pack()
boton_informativo=tk.Button(ventana_principal,text="Mostrar informacion",command=ventana_informacion)
boton_informativo.pack()

#-----Boton mensaje advertencia y etiqueta
etiqueta_warning=tk.Label(ventana_principal,text="preciona para advertencia")
etiqueta_warning.pack()
boton_warning=tk.Button(ventana_principal,text="mostar advertencia",command=ventana_adveretencia)
boton_warning.pack()

#---Btono para error y eqtieuta 
etiquta_error=tk.Label(ventana_principal,text="presiona para ventana de error")
etiquta_error.pack()
boton_erro=tk.Button(ventana_principal,text="mostrar error")
boton_erro.pack()

#----Boton mensaje pregunta si/no 
etiqueta_pregunta_sino=tk.Label(ventana_principal,text="preciona para pregunta si /no")
etiqueta_pregunta_sino.pack()
boton_pregunta_sino=tk.Button(ventana_principal,text="mostrar pregunta de si /no")
boton_pregunta_sino.pack()

#----Boton mensaje de aceptar/cancelar
etiqueta_pregunta_acepta=tk.Label(ventana_principal,text="precionar pregunta aceptar/ cancelar")
etiqueta_pregunta_acepta.pack()
boton_pregunta_aceptar=tk.Button(ventana_principal,text="mostrar pregunta acempar/cancaelar")
boton_pregunta_aceptar.pack()

#---Boton mensaje de si/no/cancelar
etiqueta_pregunta_sino_cancelar=tk.Label(ventana_principal,text="preciona para pregunta si/no/cancelar")
etiqueta_pregunta_sino_cancelar.pack()
boton_pregunta_sino_cancelar=tk.Button(ventana_principal,text="moatrar pregunta de si/no/cancelar")
boton_pregunta_sino_cancelar.pack()




#indicar el loop principla de la aplicacion 
#para mantener la ventana principal 
ventana_principal.mainloop()