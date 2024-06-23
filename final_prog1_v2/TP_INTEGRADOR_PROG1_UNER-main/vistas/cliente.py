import tkinter as tk
from tkinter import ttk
from .claseg import Frame


def open_vista_cliente(root):
    vista_cliente = tk.Toplevel(root)
    vista_cliente.title('Gestor Autos - Clientes')
    vista_cliente.iconbitmap('img/autito.ico')
    vista_cliente.resizable(0,0)

    app = Frame3(root = vista_cliente)
    app.config(background='#F7F9AF')

    close_button = tk.Button(vista_cliente, text="Close", command=vista_cliente.destroy)
    close_button.pack()

class Frame3(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()

        self.label_form()
        self.input_form()
        #self.tabla_cliente()

    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_nombre.grid(row= 1, column=0,padx=10,pady=10)

        self.label_apellido = tk.Label(self, text="Apellido:")
        self.label_apellido.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_apellido.grid(row= 1, column=3,padx=10,pady=10)

        self.label_documento = tk.Label(self, text="Documento:")
        self.label_documento.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_documento.grid(row= 2, column=0,padx=10,pady=10)

        self.label_telefono = tk.Label(self, text="Telefono:")
        self.label_telefono.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_telefono.grid(row= 2, column=3,padx=10,pady=10)

        self.label_direccion = tk.Label(self, text="Dirección:")
        self.label_direccion.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_direccion.grid(row= 3, column=0,padx=10,pady=10)

        self.label_correo = tk.Label(self, text="Correo Electronico:")
        self.label_correo.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_correo.grid(row= 4, column=0,padx=10,pady=10)

    def input_form(self):
        self.nombre_c = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.nombre_c)
        self.entry_nombre.config(width=20, font=('Arial',12))
        self.entry_nombre.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')

        self.apellido_c = tk.StringVar()
        self.entry_apellido = tk.Entry(self,textvariable=self.apellido_c)
        self.entry_apellido.config(width=20, font=('Arial',12))
        self.entry_apellido.grid(row= 1, column=4,padx=10,pady=10, columnspan='2')

        self.documento_c = tk.StringVar()
        self.entry_documento = tk.Entry(self,textvariable=self.documento_c)
        self.entry_documento.config(width=20, font=('Arial',12))
        self.entry_documento.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.telefono_c = tk.StringVar()
        self.entry_telefono = tk.Entry(self,textvariable=self.telefono_c)
        self.entry_telefono.config(width=20, font=('Arial',12))
        self.entry_telefono.grid(row= 2, column=4,padx=10,pady=10, columnspan='2')

        self.direccion_c = tk.StringVar()
        self.entry_direccion = tk.Entry(self,textvariable=self.direccion_c)
        self.entry_direccion.config(width=25, font=('Arial',12))
        self.entry_direccion.grid(row= 3, column=1,padx=10,pady=10, columnspan='3')

        self.correo_c = tk.StringVar()
        self.entry_correo = tk.Entry(self,textvariable=self.correo_c)
        self.entry_correo.config(width=50, font=('Arial',12))
        self.entry_correo.grid(row= 4, column=1,padx=10,pady=10, columnspan='4')
    
    def tabla_cliente(self):
        self.tabla = tk.Treeview(self, columns=('Nombre','Apellido','Documento','Direccion','Telefono','Correo Electronico'))
        self.tabla.grid(row=5,column=0,columnspan=6,sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=5, column=4,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Apellido')
        self.tabla.heading('#3',text='Documento')
        self.tabla.heading('#4',text='Direccion')
        self.tabla.heading('#5',text='Telefono')
        self.tabla.heading('#6',text='Correo Electronico')


        self.tabla.show("Direccion", show="hidden")
        self.tabla.show("Telefono", show="hidden")
        self.tabla.show("Correo Electronico", show="hidden")

        self.tabla.column('#1', minwidth=100)
        self.tabla.column('#2', minwidth=100)
        self.tabla.column('#3', minwidth=100)
        self.tabla.column('#4', minwidth=150)

    







