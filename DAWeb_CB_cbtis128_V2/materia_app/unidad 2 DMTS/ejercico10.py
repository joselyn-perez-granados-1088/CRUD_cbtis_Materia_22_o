import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
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

def habilitar_entry():
        if var1.get()==1:
            entrada1.config(state="normal")
            entrada1.delete(0,tk.END)
            entrada1.insert(0,0)
        else:
            entrada1.delete(0,tk.END)
            entrada1.insert(0,0)
            entrada1.config(state="disabled")
        
        if var1.get()==2:
            entrada2.config(state="normal")
            entrada2.delete(0,tk.END)
            entrada2.insert(0,0)
        else:
            entrada2.delete(0,tk.END)
            entrada2.insert(0,0)
            entrada2.config(state="disabled")

        
        if var1.get()==3:
            entrada3.config(state="normal")
            entrada3.delete(0,tk.END)
            entrada3.insert(0,0)
        else:
            entrada3.delete(0,tk.END)
            entrada3.insert(0,0)
            entrada3.config(state="disabled")


            
def limpiar():
    entrada1.delete(0,tk.END)
    entrada2.delete(0,tk.END)
    entrada3.delete(0,tk.END)
    entrada1.insert(0,0)
    entrada2.insert(0,0)
    entrada3.insert(0,0)
    var1.set(0)
    var2.set(0)

def convertir():
    try:
        centigrados=float(entrada1.get())
        fareheit=float(entrada2.get())
        kelvin=float(entrada3.get())
        var1_seleccion=var1.get()
        var2_seleccion=var2.get()
        if var1_seleccion==var2_seleccion:
            messagebox.showwarning("adevertencia","debes seleccionar unidades diferentes")
        elif centigrados== 0 and fareheit ==0 and kelvin==0:
            messagebox.showwarning("advertencia0","introduce un dato diferente")
        elif var1_seleccion== "centigrados" and var2_seleccion == "fareheit":
            operacion=centigrados*(9/5)+32
            entrada2.config(state="normal")
            entrada2.insert(0,operacion)
            entrada2.config(state="readonly")
        elif var1_seleccion== "centigrados" and var2_seleccion == "kelvin":
            operacion=centigrados+273.15
            entrada3.config(state="normal")
            entrada2.insert(0,operacion)
            entrada3.config(state="readonly")
        elif var1_seleccion== "farenheit" and var2_seleccion == "centigrados":
            operacion=(fareheit-32)*(5/9)
            entrada1.config(state="normal")
            entrada1.insert(0,operacion)
            entrada1.config(state="readonly")
        elif var1_seleccion== "fareheit" and var2_seleccion == "kelvin":
            operacion=(fareheit+459.67)*(5/9)
            entrada3.config(state="normal")
            entrada3.insert(0,operacion)
            entrada3.config(state="readonly")
        elif var1_seleccion== "kelvin" and var2_seleccion == "centigrados":
            operacion=kelvin-273.15
            entrada1.config(state="normal")
            entrada1.insert(0,operacion)
            entrada1.config(state="readonly")
        elif var1_seleccion== "kelvin" and var2_seleccion == "fareheit":
            operacion=(kelvin-273.15)*(9/5)+32
            entrada2.config(state="normal")
            entrada2.insert(0,operacion)
            entrada2.config(state="readonly")
        elif var1_seleccion== "centigrados" and var2_seleccion == "todos":
            entrada2.config(state="normal")
            entrada3.config(state="normal")
            operacion=(centigrados * (9/5))+32   
            operacion=centigrados+273.15
            entrada2.insert(0,operacion)         
            entrada3.insert(0,operacion)  
            entrada2.config(state="readonly")
            entrada3.config(state="readonly")       
        elif var1_seleccion== "farehit" and var2_seleccion == "todos":
            entrada1.config(state="normal")
            entrada3.config(state="normal")
            operacion=(fareheit - 32)*(5/9)
            operacion=(fareheit +459.67)*(5/9)
            entrada1.insert(0,operacion)         
            entrada3.insert(0,operacion)  
            entrada1.config(state="readonly")
            entrada3.config(state="readonly")       
        elif var1_seleccion== "klevin" and var2_seleccion == "todos":
            entrada1.config(state="normal")
            entrada2.config(state="normal")
            operacion=kelvin-273.15 
            operacion=(kelvin-273.15)*(9/5)+32
            entrada1.insert(0,operacion)         
            entrada2.insert(0,operacion)  
            entrada1.config(state="readonly")
            entrada3.config(state="readonly")       
            
            
    except ValueError:
        messagebox.showwarning("error","ingrese valor valido")



#creamos la ventana principal 
ventana_principal=tk.Tk()
#titulo de la ventana 
ventana_principal.title("Ejercicio 10")
#definir tamaño de ventana 
ventana_principal.geometry("300x400")

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
ventana_principal.geometry(f"300x400+{x_coordinante}+{y_coordinante}")

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



etiqueta2=tk.Label(ventana_principal,text="centigrados" )
etiqueta2.grid(row=0,column=0)
#entrada1
entrada1=tk.Entry(ventana_principal,state="disabled")
entrada1.insert(0,"0")
entrada1.config(state="readonly")
entrada1.grid(row=1,column=0)


#etiqueta2
etiqueta3=tk.Label(ventana_principal,text="Farenheit")
etiqueta3.grid(row=2,column=0)

#entrada3
entrada2=tk.Entry(ventana_principal,state="disabled")
entrada2.insert(0,"0")
entrada2.config(state="readonly")
entrada2.grid(row=3,column=0)


#etiqueta4
etiqueta4=tk.Label(ventana_principal,text="Kelvin")
etiqueta4.grid(row=4,column=0)


entrada3=tk.Entry(ventana_principal,state="disabled")
entrada3.insert(0,"0")
entrada3.config(state="readonly")
entrada3.grid(row=5,column=0)


#etiqueta4
etiqueta1=tk.Label(ventana_principal,text="Selecciona la unidad " )
etiqueta1.grid(row=0,column=1)



#-----Radiobuton 
#creae variable que almacenar el valor seleccionado 
var1=tk.IntVar()

radio1=tk.Radiobutton(ventana_principal,text="celsius", variable=var1, value=1,command=habilitar_entry)
radio1.grid(row=6,column=1)
radio2=tk.Radiobutton(ventana_principal, text="farenheit", variable=var1, value=2,command=habilitar_entry)
radio2.grid(row=7,column=1)
radio3=tk.Radiobutton(ventana_principal, text="kelvin", variable=var1, value=3,command=habilitar_entry)
radio3.grid(row=8,column=1)

#valor por default de varaible para almacenar valores 
var1.set("celsius")


#etiqueta4
etiqueta1=tk.Label(ventana_principal,text="Selecciona la unidad a convertir" )
etiqueta1.grid(row=9,column=1)

#-----Radiobuton dos
#creae variable que almacenar el valor seleccionado 
var2=tk.IntVar()

radio4=tk.Radiobutton(ventana_principal,text="celsius", variable=var2, value=1,command=habilitar_entry)
radio4.grid(row=10,column=1)

radio5=tk.Radiobutton(ventana_principal, text="farenheit", variable=var2, value=2,command=habilitar_entry)
radio5.grid(row=11,column=1)
radio6=tk.Radiobutton(ventana_principal, text="kelvin", variable=var2, value=3,command=habilitar_entry)
radio6.grid(row=12,column=1)

#valor por default de varaible para almacenar valores 
var2.set("celsius")



#Botones 
botones_convertir=tk.Button(ventana_principal,text="convertir",command=convertir)
botones_convertir.grid()
botones_limpiar=tk.Button(ventana_principal,text="limpiar",command=limpiar)
botones_limpiar.grid()




ventana_principal.mainloop()










































#mendeaj en la ventana de que no piedes seleccionar igual 