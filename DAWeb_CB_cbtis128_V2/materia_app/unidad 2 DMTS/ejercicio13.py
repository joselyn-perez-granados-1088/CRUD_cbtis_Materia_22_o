#importamos libreria 
import tkinter as tk 
from tkinter import messagebox
from tkinter import ttk
#funcion salir 
#define el proceso de la vemtama principal y cerrrar el programa 
def salir():
    ventana_principal.quit()

#Funcion de pantalla principal 
def pantalla_s():
    ventana_principal.geometry("300x200")

def pantalla_m():
    ventana_principal.geometry("600x400")

def pantalla_g():
    ventana_principal.geometry("1020x800")

def habilita_entry(event):
    #creamos nuetra variables que almacenara el valor seleccionado  
    # conbobox que contiene los valores despegabeles 
    #un get que es el valor seleccionado actualmente en el conbobox
    opciones_selecciona=cb1.get()
    #validar la opcion seleccionada paramhabilitar radiobotones 
    #opcion 1, utilizar el operador no igual diferente ya que la opcion selecionada 
    #al iniciar es igual a vacio(**):
    #opcion2, ess convertir los que se ontiene del combobox a entero 
    #y realizar la validacion 
    #if opciones_seleccionada !=""
    if opciones_selecciona !="":
        #establecemos los radios para que permita al usuario seleccionarlos
        radio1.config(state="normal")
        radio2.config(state="normal")
        radio3.config(state="normal")
    else:#establecemos un radio con disabled para que impida que el usuario lo seleccione
        radio1.config(state="disabled")
        radio2.config(state="disabled")
        radio3.config(state="disabled")

def limpiar():
    #limpiamos entrada
    cb1.delete(0,tk.END)
    #Establecemos los radios desabilitados, para que el usuario no pueda seleccionar esa opcion
    radio1.config(state="disabled")
    radio2.config(state="disabled")
    radio3.config(state="disabled")
    #Establecemos el conbobox a cero que significa que se seleccionara el primer elemento
    cb1.current(0)
    #Asignamos los valores a una variable tipo var.set para almacenar las variables
    var.set("camisa $300")
    var.set("pantalon $250")
    var.set("calcetines $100")

def comparar():
    try:
        #obtenemos el valor seleccionado actualmente con el conbobox
        opciones_seleccionada=cb1.get()
        #obtenemos el valor seleccionado actual del radiobutton
        radioboton_seleccionada=var.get()
         
         
         #-----------------camisa--------------------------
        #
        #el descunato de 15 porcineto de camisa
        if opciones_seleccionada=="camisa $300" and radioboton_seleccionada =="15":
            resul=(300)-(300*(15/100)) 
            messagebox.showinfo("El descuento de tu camisa es:",f"El precio final de tu camisa es:{resul}")
        #el 10 porcinto de descuento de camisa
        elif opciones_seleccionada=="camisa $300" and radioboton_seleccionada =="10":
                resul=(300)-(300*(10/100))
                messagebox.showinfo("El descuento de tu camisa es:",f"El precio final de tu camisa es:{resul}")
        #el 5 porcinto de descuanto de camisa
        elif opciones_seleccionada=="camisa $300" and radioboton_seleccionada =="5":
                resul=(300)-(300*(5/100))
                messagebox.showinfo("El descuento de tu camisa es:",f"El precio final de tu camisa es:{resul}")
         #el precio de camisa sin el descunato 
        elif opciones_seleccionada=="camisa $300":
            messagebox.showinfo("Tu compra exitosa es","Compraste una camisa por:$300")

        #-----------Pantalon------------
        
        #el 15 por ciento del pantalon
        elif  opciones_seleccionada=="Pantalon $250" and  radioboton_seleccionada=="15":
                resul1=(250)-(250*(15/100))
                messagebox.showinfo("El descuanto de tu pantaon es:",f"El precio final de tu pantalon es:{resul1}")
        #el 10 porciento de descuento del pantalon 
        elif  opciones_seleccionada=="Pantalon $250" and  radioboton_seleccionada=="10":
                resul1=(250)-(250*(10/100))
                messagebox.showinfo("El descuanto de tu pantaon es:",f"El precio final de tu pantalon es:{resul1}")
        #el 5 por ciento del pntalon 
        elif  opciones_seleccionada=="Pantalon $250" and  radioboton_seleccionada=="5":
                resul1=(250)-(250*(5/100))
                messagebox.showinfo("El descuanto de tu pantaon es:",f"El precio final de tu pantalon es:{resul1}")
        #el precio del pantalon sin el descunato 
        elif opciones_seleccionada=="Pantalon $250":
            messagebox.showinfo("Tu compra exitosa es","Compraste un Pantalon por:$250")

        
        #-------------calsetines---------------
        
         #el 15 por ciento de los calisetines 
        elif opciones_seleccionada=="calsetines $100" and radioboton_seleccionada=="15":
                resul2=(100)-(100*(15/100))
                messagebox.showinfo("El descuanto de tus calcetines es:",f"El precio final de tus calcetines es:{resul2}")
        #el 10 porciento de los calcetines
        elif opciones_seleccionada=="calsetines $100" and radioboton_seleccionada=="10":
                resul2=(100)-(100*(10/100))
                messagebox.showinfo("El descuanto de tus calcetines es:",f"El precio final de tus calcetines es:{resul2}")
        #el 5 porciento de descuento del los calcetines
        elif opciones_seleccionada=="calsetines $100" and radioboton_seleccionada=="5":
            resul2=(100)-(100*(5/100))
            messagebox.showinfo("El descuanto de tus calcetines es:",f"El precio final de tus calcetines es:{resul2}")
        #el precio de los calsetines sin el descunato 
        elif opciones_seleccionada=="calsetines $100":
            messagebox.showinfo("Tu compra exitosa es","Compraste unos calsetines por:$100")

            
    except ValueError:
        messagebox.showerror("Error","Es una opcion no valida")



#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("ejercicio 4")
#definir tamaño de ventana 
ventana_principal.geometry("550x300")

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
ventana_principal.geometry(f"550x300+{x_coordinante}+{y_coordinante}")

#crear la barra de Menu
barra_principal=tk.Menu(ventana_principal)

#----Submenu opciones-----
#definimoa submenu dentro de menu principal 
menu_opciones=tk.Menu(barra_principal,tearoff=0)
menu_opciones.add_command(label="Nuevo")
menu_opciones.add_command(label="Abriri")
menu_opciones.add_separator()

#asignamos una funcion a la opcion salir 
menu_opciones.add_command(label="salir",command=salir)

#------Submenu tamaño-----
menu_saize=tk.Menu(barra_principal,tearoff=1)
menu_saize.add_command(label="300x200",command=pantalla_s)
menu_saize.add_command(label="600x400",command=pantalla_m)
menu_saize.add_command(label="1020x800",command=pantalla_g)

#--------Agregamos de submenu a barra principal
#agregar el menu opciones a la barra principal
barra_principal.add_cascade(label="opciones",menu=menu_opciones)
barra_principal.add_cascade(label="tamaño",menu=menu_saize)
ventana_principal.config(menu=barra_principal)



#---------componentes 
#etiqueta1
etiqueta1=tk.Label(ventana_principal,text="Ropa ")
etiqueta1.grid()

opciones=["Seleciona una opcion","camisa $300","Pantalon $250","calsetines $100"]
cb1=ttk.Combobox(ventana_principal, values=opciones)
cb1.grid()
#establecer la opcion determinada 
cb1.current(0)
#llamar la fumcion  seleccionar
cb1.bind("<<ComboboxSelected>>",habilita_entry)


#etiqueta1
etiqueta1=tk.Label(ventana_principal,text="Descuento")
etiqueta1.grid()

#-----Radiobuton 
#creae variable que almacenar el valor seleccionado 
var=tk.StringVar()

radio1=tk.Radiobutton(ventana_principal,text="15", variable=var, value="15",state="disabled")
radio1.grid()
radio2=tk.Radiobutton(ventana_principal, text="10", variable=var, value="10",state="disabled")
radio2.grid()
radio3=tk.Radiobutton(ventana_principal, text="5", variable=var, value="5",state="disabled")
radio3.grid()

#valor por default de varaible para almacenar valores 
var.set(0)



#Botones 
botones_resultado=tk.Button(ventana_principal,text="comprar",command=comparar)
botones_resultado.grid(row=10, column=0,padx=5, pady=5)
botones_limpiar=tk.Button(ventana_principal,text="limpiar",command=limpiar)
botones_limpiar.grid(row=10, column=2,padx=5, pady=5)




ventana_principal.mainloop()