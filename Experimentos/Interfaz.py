from tkinter import *
import sys
import shutil
import os 
from PIL import ImageTk, Image
global Ruta, Ruta2

class Menu: 
    def __init__(self, master):
        
        
        root.geometry("1091x590") # Se establece el alto y el largo de la ventana
        root.config(bg="white") # El color de fondo
        self.master = master 
        master.title("Gestor de archivos EF") # El titulo de la ventana
        self.ir=0




        #### Creacion de la lista con los archivos
        self.ar=[]
        ejemplo_dir = os.path.dirname(__file__)
        with os.scandir(ejemplo_dir) as ficheros:
            for fichero in ficheros:
                self.ar.append(fichero.name)
        self.ar.remove(os.path.basename(__file__))
        ####


        self.img = Image.open(self.ar[self.ir])   # Abre la imagen correspondiente a current_image
        self.img = self.img.resize((300, 300), Image.ANTIALIAS)   # Escala la imagen a 300x300
        self.photo = ImageTk.PhotoImage(self.img)                # Crea un objeto PhotoImage a partir de la imagen
        self.Tetardas= Label(image=self.photo)
        self.Tetardas.place(x=300, y=400)

        

        self.Tetas= Label(master, text=self.ar[self.ir])
        self.Tetas.place(x=100, y=200)
        # Prueba de la funcion mover (NO COMPLETADO)
        
        
        self.BM = Button(master, text="mover",height = 1,width = 5, command=lambda:[ self.mover(), self.mostrar_siguiente()]) # Se crea un boton para cerrar el menu
        self.BM.config(font=("impact", 18)) 
        self.BM.place(x=30, y=100)


        self.BM2 = Button(master, text="mover",height = 1,width = 5, command=self.mover2) # Se crea un boton para cerrar el menu
        self.BM2.config(font=("impact", 18)) 
        self.BM2.place(x=30, y=200)
        
        
        
        # Boton Cerrar
        
        self.botonCerrar = Button(master, text="Cerrar",height = 1,width = 5, command=self.cerrar) # Se crea un boton para cerrar el menu
        self.botonCerrar.config(font=("impact", 18)) 
        self.botonCerrar.place(x=30, y=50)

        
    
    def mover (self):
        
        shutil.move(self.ar[self.ir], Ruta )
        

    def mover2 (self):
        print("Estoy funcionando!")
        shutil.move(self.ar[self.ir], Ruta2)


    def mostrar_siguiente(self):
        # Avanzamos el índice
        self.ir += 1
        
        # Si llegamos al final de la lista, volvemos al principio
        if self.ir == len(self.ar):
            self.Tetas.config(text="NO QUEDAN MAS ELEMENTOS")
        else:
            # Actualizamos el texto del Label con el elemento actual
            self.Tetas.config(text=self.ar[self.ir])
            self.img = Image.open(self.ar[self.ir])   # Abre la imagen correspondiente a current_image
            self.img = self.img.resize((300, 300), Image.ANTIALIAS)   # Escala la imagen a 300x300
            self.photo = ImageTk.PhotoImage(self.img)                # Crea un objeto PhotoImage a partir de la imagen
            self.Tetardas.config(image=self.photo)


    
    def cerrar(self): # En caso de que el usuario use el boton cerrar se llama esta funcion
       
        sys.exit() # Funcion sys para cerrar el programa


Ruta=input("Ingrese la ruta destinada a la primera carpeta: ")
Ruta2=input("Ingrese la ruta destinada a la primera carpeta: ")
root = Tk() # Variable Raiz
miVentana = Menu(root) # La variable raiz es modificada por la clase Menu
root.mainloop() # Funcion de Tkinter para mostrar la ventana