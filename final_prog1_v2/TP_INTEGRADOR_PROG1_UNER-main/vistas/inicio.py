import tkinter as tk
from tkinter import ttk

from .cliente import open_vista_cliente
from .vehiculos import open_vista_vehiculos
from .transacciones import open_vista_transacciones
from .claseg import Frame


def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu = barra, width = 300 , height = 300)
    menu_inicio = tk.Menu(barra, tearoff=0)

    #  niveles  #

    #principal

    barra.add_cascade(label='Inicio', menu = menu_inicio)
    barra.add_cascade(label='Consultas')
    barra.add_cascade(label='Acerca de..')
    barra.add_cascade(label='Ayuda')

    #submenu
    menu_inicio.add_command(label='ABM Cliente', command = lambda: open_vista_cliente(root))
    menu_inicio.add_command(label='ABM Vehiculos', command = lambda: open_vista_vehiculos(root))
    menu_inicio.add_command(label='ABM Transacciones', command = lambda: open_vista_transacciones(root))
    menu_inicio.add_command(label='Salir', command= root.destroy)


class Frame2(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()

        self.label_principal()
        self.botonera_principal(root)

    def label_principal(self):
        self.label_titulo = tk.Label(self, text="Sistema de Gestion Automotriz ")
        self.label_titulo.config(font=('Arial',15,'bold'))
        self.label_titulo.grid(row= 1, column=0,padx=10,pady=10, columnspan=4)

        self.label_version = tk.Label(self, text="V0.1 ")
        self.label_version.config(font=('Arial',10,'bold'))
        self.label_version.grid(row= 5, column=4,padx=10,pady=10)
    
    def botonera_principal(self,root):
        self.btn_cliente = tk.Button(self, text='Cliente', command=lambda: open_vista_cliente(root))
        self.btn_cliente.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_cliente.grid(row= 2, column=0,padx=10,pady=10)

        self.btn_vehiculos = tk.Button(self, text='Vehiculos', command=lambda: open_vista_vehiculos(root))
        self.btn_vehiculos.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_vehiculos.grid(row= 2, column=2,padx=10,pady=10)

        self.btn_transacciones = tk.Button(self, text='Transacciones', command=lambda: open_vista_transacciones(root))
        self.btn_transacciones.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_transacciones.grid(row= 2, column=4,padx=10,pady=10)


