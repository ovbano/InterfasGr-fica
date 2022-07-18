import webbrowser
import pymongo
from tkinter import *

miUsuario=pymongo.MongoClient("mongodb://localhost:27017/")
basedatos=miUsuario["Beneficiarios"]
colleccion=basedatos["Acreditados"]

campos=Tk()
campos.title("-------Acreditate-------")
campos.geometry("600x400")
campos.iconbitmap("prestamo.ico")
campos.config(bg = "gray94")
#agrandar la ventana, abajo arriba, izquierda derecha
campos.resizable(0,0)

def evaluar():
    ventanaEmergente=Toplevel()
    ventanaEmergente.title('DATOS DEL ACREDITADO')
    ventanaEmergente.geometry("600x400")

    frame2 = Frame(ventanaEmergente ,width=600, height= 400)
    frame2.config(bg='gray94')
    frame2.config(bd= 75)
    
    datosUsuario = (colleccion.find_one({'nombre':'Juan'},{'_id':0,'nombre':1}))
    Label(ventanaEmergente, text=datosUsuario).grid(row=0, column=0)
    Entry(ventanaEmergente, text=datosUsuario, state='disable').grid(row=0, column=1)

usuario=Frame(campos, width= "600", height= "400")
usuario.pack()

cuadroN=Entry(usuario)
cuadroN.grid(row=0, column=1)
cuadroN.config(justify="center",font = ("Arial",11))
cuadroN.focus()

cuadroA=Entry(usuario)
cuadroA.grid(row=1, column=1)
cuadroA.config(justify="center",font = ("Arial",11))
cuadroA.focus()

cuadroId=Entry(usuario)
cuadroId.grid(row=2, column=1)
cuadroId.config(justify="center",font = ("Arial",11))
cuadroId.focus()

nombre=Label(usuario,text="Nombre")
nombre.grid(row=0, column=0, padx=10, pady=10)
nombre.focus()

apellido=Label(usuario,text="Apeliido")
apellido.grid(row=1, column=0, padx=10, pady=10)
apellido.focus()

id=Label(usuario,text="Número de cédula")
id.grid(row=2, column=0, padx=10, pady=10)
id.focus()

buscar = Button(usuario, text='Evaluar', command=evaluar,bg = "gray88", fg="black", font = ("Arial",11)).grid(row=4, columnspan=3)

def github():
        webbrowser.open("www..com")
myvercion = Button(campos, text = "Vercionamiento", bg = "gold", fg = "black", command = github, cursor = "circle", font = ("Arial",14)).pack(pady=20)

campos.mainloop()


