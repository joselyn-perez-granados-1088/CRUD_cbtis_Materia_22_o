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
def ventana_error():
    messagebox.showerror("error","esre es un ,ensaje de error")

#funcion para preguntar si/no 
def ventana_sino():
    #usamos variable para guardar la respuesta de la pregunta 
    #ventana emergente
    respuesta =messagebox.askquestion("confirmacion si/no","¿deseas continuar?")
    #validar respuesta
    if respuesta== 'yes':
        print("el usuario selecciona si")
    else:
        print("el ususario selecciona no")

#funcion para preguntar acempar/cancelar 
def ventana_aceptar():
    #ventana emergente
    respuesta=messagebox.askokcancel("confirmacion aceptar/cancelar","¿deseas continuarm")
    #valida respuesta
    if respuesta:
        print("el usuario selecciona aceptar")
    else:
        print("el usuario selecciono cancelar")

#funcion para preguntar si/no/cancelar
def ventana_sino_cancelar():
    #ventana emergente
    respuesta=messagebox.askretrycancel("confirmacion si/no/cancelar","¿deseas continuarm")
    #valida respuesta
    if respuesta is True:
        print("el usuario selecciono si")
    elif respuesta is False:
        print("el usuario selecciono no")
    else:
        print("EL usuario selecciono cancelar")


#creamos ventana principal 
ventana_principal=tk.Tk()

#establecemos titulo a la ventana principal
ventana_principal.title("ventana principal")

#definimos la dimencion de la ventana principla 
ventana_principal.geometry("300x450")

#-----  Boton mensaje informativo y eqtiqueta
etiqueta_info=tk.Label(ventana_principal,text="preciona para ventana de informacion")
etiqueta_info.pack(pady=5)
boton_informativo=tk.Button(ventana_principal,text="Mostrar informacion",command=ventana_informacion)
boton_informativo.pack(pady=5)

#-----Boton mensaje advertencia y etiqueta
etiqueta_warning=tk.Label(ventana_principal,text="preciona para advertencia")
etiqueta_warning.pack(pady=5)
boton_warning=tk.Button(ventana_principal,text="mostar advertencia",command=ventana_adveretencia)
boton_warning.pack(pady=5)

#---Btono para error y eqtieuta 
etiquta_error=tk.Label(ventana_principal,text="presiona para ventana de error")
etiquta_error.pack(pady=5)
boton_erro=tk.Button(ventana_principal,text="mostrar error",compound=ventana_error)
boton_erro.pack(padx=5)

#----Boton mensaje pregunta si/no 
etiqueta_pregunta_sino=tk.Label(ventana_principal,text="preciona para pregunta si /no")
etiqueta_pregunta_sino.pack(padx=5)
boton_pregunta_sino=tk.Button(ventana_principal,text="mostrar pregunta de si /no",compound=ventana_sino)
boton_pregunta_sino.pack(pady=5)

#----Boton mensaje de aceptar/cancelar
etiqueta_pregunta_acepta=tk.Label(ventana_principal,text="precionar pregunta aceptar/ cancelar")
etiqueta_pregunta_acepta.pack(pady=5)
boton_pregunta_aceptar=tk.Button(ventana_principal,text="mostrar pregunta acempar/cancaelar",command=ventana_aceptar)
boton_pregunta_aceptar.pack(pady=5)

#---Boton mensaje de si/no/cancelar
etiqueta_pregunta_sino_cancelar=tk.Label(ventana_principal,text="preciona para pregunta si/no/cancelar")
etiqueta_pregunta_sino_cancelar.pack(pady=5)
boton_pregunta_sino_cancelar=tk.Button(ventana_principal,text="moatrar pregunta de si/no/cancelar",compound=ventana_sino_cancelar)
boton_pregunta_sino_cancelar.pack(pady=5)

#indicar el loop principla de la aplicacion 
#para mantener la ventana principal 
ventana_principal.mainloop()    