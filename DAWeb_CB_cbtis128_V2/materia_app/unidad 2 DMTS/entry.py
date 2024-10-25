#importes de libreria
import tkinter as tk
def obtener_info():
  texto_obtenido=txt2.get()
  print(texto_obtenido)

def limpiar_entry():
  txt7.delete(0,tk.END)
#decalramos vcentana primcipal
ventana_principal=tk.Tk()
ventana_principal.title("entrada de texto")
#definimos dimencion
ventana_principal.geometry("300x200")
#-----entry basico-----------
etiqueta1=tk.Label(text="Entrada basica")
etiqueta1.pack()


#obtener widget entry en ventana principal
text1=tk.Entry(ventana_principal)
text1.pack(pady=10)
#------entry obtener de informacion---------
etiquta2=tk.Label(text="obtener info de entra")
etiquta2.pack()

txt2=tk.Entry(ventana_principal)
txt2.pack()

boton_txt2=tk.Button(ventana_principal,
text="obtener texto",
command=obtener_info)
boton_txt2.pack()    

etiqueta3=tk.Label(text="valor inicial en entry")
etiqueta3.pack()
text3=tk.Entry(ventana_principal)
text3.pack()
text3.insert(0,"escribe lgo porfavor")

etiqueta4=tk.Label(text="ancho especifico")
etiqueta4.pack()
txt4=tk.Entry(ventana_principal,width=40)
txt4.pack()

etiqueta5=tk.Label(text="entry contraseña")
etiqueta5.pack()
txt5=tk.Entry(ventana_principal,show="*")
txt5.pack()
etiqueta6=tk.Label(text="entry desabilitado")
etiqueta6.pack()

txt6=tk.Entry(ventana_principal,state="disabled")
txt6.pack()

etiqueta7=tk.Label(text="limpiar entry")
etiqueta7.pack()
txt7=tk.Entry(ventana_principal)
txt7.pack()

boton_txt7=tk.Button(ventana_principal,text="limpiar",command=limpiar_entry)
boton_txt7.pack()
ventana_principal.mainloop()
