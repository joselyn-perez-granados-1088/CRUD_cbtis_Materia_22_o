#decalracion de ventanas principal con lubreria tkinter 
#imprimir lobreria tkinter 
#mandamos a mandar a llamr la libreria y le asiganamos un nombre 
#al objetivo para utilizarlo en el codugo , llamado tk
import tkinter as tk 
#decalracioj de funcion 
def ventana_sec():
    #decalrar la ventana secundaria con toplevel
    ventana_secundaria=tk.Toplevel(ventana)
    #establecemos el titulo a la ventana secuandaira
    ventana_secundaria.title("ventana secuandaria")
    #definimos la dimencion de la ventana secuandaira
    ventana_secundaria.geometry("300x200")
    #decalaramos un etiqueta con instrucciones 
    etiqueta2=tk.Label(ventana_secundaria, text="Esta es una ventana")
    #empaquetar la etiqueta para empezar la ventana
    etiqueta2.pack()
#termina funcion 

#creamos ventana principal 
ventana=tk.Tk()

#establecemos titulo a la ventana principal
ventana.title("ventana principal")

#definimos la dimencion de la ventana principla 


#decalracion de un etiqueta con instrucciones 
etiqueta1= tk.Label(ventana,text="puschale al boton",font=("century",25))

#empaquetar la etiqieta para que aparesaca en la ventana
etiqueta1.pack()

#decalramos boton para  mandar a llamar ventana secucndaria 
boton1= tk.Button(ventana,text="puchame",command=ventana_sec,font=("arial",20))

#empaquetar el boton para que aparezca en la ventana
boton1.pack()

#indicar el loop principla de la aplicacion 
#para mantener la ventana principal 
ventana.mainloop()  