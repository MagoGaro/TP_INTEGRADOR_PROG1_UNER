import tkinter as tk
from tkinter import ttk
from vistas.claseg import Frame


def open_vista_vehiculos(root):
    vista_vehiculos = tk.Toplevel(root)
    vista_vehiculos.title('Gestor Autos - Vehiculos')
    vista_vehiculos.iconbitmap('img/autito.ico')
    vista_vehiculos.resizable(0,0)

    # Add widgets to the secondary window here
    app = Frame4(root = vista_vehiculos)
    app.config(background='#F7F9AF')

    # Create a button to close the secondary window
    close_button = tk.Button(vista_vehiculos, text="Close", command=vista_vehiculos.destroy)
    close_button.pack()

class Frame4(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()

        self.label_form()
        self.input_form()
        self.tabla_cliente()

    def label_form(self):
        self.label_patente = tk.Label(self, text="Nº de Patente:")
        self.label_patente.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_patente.grid(row= 1, column=0,padx=10,pady=10)

        self.label_marca = tk.Label(self, text="Marca:")
        self.label_marca.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_marca.grid(row= 1, column=3,padx=10,pady=10)

        self.label_modelo = tk.Label(self, text="Modelo:")
        self.label_modelo.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_modelo.grid(row= 2, column=3,padx=10,pady=10)

        self.label_tipo = tk.Label(self, text="Tipo:")
        self.label_tipo.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_tipo.grid(row= 2, column=0,padx=10,pady=10)

        self.label_anio = tk.Label(self, text="Año:")
        self.label_anio.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_anio.grid(row= 4, column=0,padx=10,pady=10)

        self.label_kilomegraje = tk.Label(self, text="Kilometraje:")
        self.label_kilomegraje.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_kilomegraje.grid(row= 4, column=3,padx=10,pady=10)

        self.label_precio_compra = tk.Label(self, text="Precio de Compra:")
        self.label_precio_compra.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_precio_compra.grid(row= 6, column=0,padx=10,pady=10)

        self.label_precio_venta = tk.Label(self, text="Precio de Venta:")
        self.label_precio_venta.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_precio_venta.grid(row= 6, column=3,padx=10,pady=10)

        self.label_estado = tk.Label(self, text="Estado:")
        self.label_estado.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_estado.grid(row= 8, column=0,padx=10,pady=10)

        

    def input_form(self):
        self.patente_c = tk.StringVar()
        self.entry_patente = tk.Entry(self,textvariable=self.patente_c)
        self.entry_patente.config(width=20, font=('Arial',12))
        self.entry_patente.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')

        self.marca_c = tk.StringVar()
        self.entry_marca = tk.Entry(self,textvariable=self.marca_c)
        self.entry_marca.config(width=20, font=('Arial',12))
        self.entry_marca.grid(row= 1, column=4,padx=10,pady=10, columnspan='2')
        
        self.modelo_c = tk.StringVar()
        self.entry_modelo = tk.Entry(self,textvariable=self.modelo_c)
        self.entry_modelo.config(width=20, font=('Arial',12))
        self.entry_modelo.grid(row= 2, column=4,padx=10,pady=10, columnspan='2')

        self.tipo_c = tk.StringVar()
        self.entry_tipo = tk.Entry(self,textvariable=self.tipo_c)
        self.entry_tipo.config(width=20, font=('Arial',12))
        self.entry_tipo.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.anio_c = tk.StringVar()
        self.entry_anio = tk.Entry(self,textvariable=self.anio_c)
        self.entry_anio.config(width=20, font=('Arial',12))
        self.entry_anio.grid(row= 4, column=1,padx=10,pady=10, columnspan='2')

        self.kilometraje_c = tk.StringVar()
        self.entry_kilometraje = tk.Entry(self,textvariable=self.kilometraje_c)
        self.entry_kilometraje.config(width=20, font=('Arial',12))
        self.entry_kilometraje.grid(row= 4, column=4,padx=10,pady=10, columnspan='4')

        self.precio_compra_c = tk.StringVar()
        self.entry_precio_compra = tk.Entry(self,textvariable=self.precio_compra_c)
        self.entry_precio_compra.config(width=20, font=('Arial',12))
        self.entry_precio_compra.grid(row=6, column=1,padx=10,pady=10, columnspan='2')

        self.precio_venta_c = tk.StringVar()
        self.entry_precio_venta = tk.Entry(self,textvariable=self.precio_venta_c)
        self.entry_precio_venta.config(width=20, font=('Arial',12))
        self.entry_precio_venta.grid(row= 6, column=4,padx=10,pady=10, columnspan='3')

        self.estado_var = tk.StringVar()
        self.entry_estado = ttk.OptionMenu(self, self.estado_var, "Estado", "Disponible", "Reservado", "Vendido")
        self.entry_estado.grid(row=8, column=1, padx=10, pady=10)
    
    def tabla_cliente(self):
        self.tabla = ttk.Treeview(self, columns=('Nº de Patente','Marca','Tipo','Anio','Modelo','Kilometraje','Precio Compra', 'Precio Venta', 'Estado'), show='headings')
        self.tabla.grid(row=9, column=0, columnspan=6, sticky='nsew')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=9, column=6, sticky='ns')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('Nº de Patente', text='Nº de Patente')
        self.tabla.heading('Marca', text='Marca')
        self.tabla.heading('Tipo', text='Tipo')
        self.tabla.heading('Anio', text='Año')
        self.tabla.heading('Modelo', text='Modelo')
        self.tabla.heading('Kilometraje', text='Kilometraje')
        self.tabla.heading('Precio Compra', text='Precio Compra')
        self.tabla.heading('Precio Venta', text='Precio Venta')
        self.tabla.heading('Estado', text='Estado')

        
        self.tabla.column('Nº de Patente', minwidth=80, width=100)
        self.tabla.column('Marca', minwidth=80, width=100)
        self.tabla.column('Tipo', minwidth=60, width=80)
        self.tabla.column('Anio', minwidth=60, width=80)
        self.tabla.column('Modelo', minwidth=80, width=100)
        self.tabla.column('Kilometraje', minwidth=80, width=100)
        self.tabla.column('Precio Compra', minwidth=100, width=110)
        self.tabla.column('Precio Venta', minwidth=100, width=110)
        self.tabla.column('Estado', minwidth=80, width=90)

        











