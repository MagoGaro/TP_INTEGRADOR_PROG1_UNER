import tkinter as tk
from vistas.claseg import Frame


def open_vista_transacciones(root):
    vista_transacciones = tk.Toplevel(root)
    vista_transacciones.title('Gestor Autos - Transacciones')
    vista_transacciones.iconbitmap('img/autito.ico')
    vista_transacciones.resizable(0,0)

    # Add widgets to the secondary window here
    app = Frame3(root = vista_transacciones)

    # Create a button to close the secondary window
    close_button = tk.Button(vista_transacciones, text="Close", command=vista_transacciones.destroy)
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

        self.label_id_de_vehículo = tk.Label(self, text="ID de Vehículo:")
        self.label_id_de_vehículo.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_id_de_vehículo.grid(row= 1, column=3,padx=10,pady=10)

        self.label_id_de_cliente = tk.Label(self, text="ID de Cliente:")
        self.label_id_de_cliente.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_id_de_cliente.grid(row= 2, column=0,padx=10,pady=10)

        self.label_tipo_de_transaccion = tk.Label(self, text="Tipo de Transaccion(Compra/Venta):")
        self.label_tipo_de_transaccion.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_tipo_de_transaccion.grid(row= 2, column=3,padx=10,pady=10)

        self.label_fecha = tk.Label(self, text="Fecha:")
        self.label_fecha.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_fecha.grid(row= 3, column=0,padx=10,pady=10)

        self.label_Monto = tk.Label(self, text="Monto:")
        self.label_Monto.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_Monto.grid(row= 3, column=3,padx=10,pady=10)

        self.label_observaciones = tk.Label(self, text="Observaciones:")
        self.label_observaciones.config(font=('Arial',12,'bold'),background='#F7F9AF')
        self.label_observaciones.grid(row= 4, column=0,padx=10,pady=10)

    def input_form(self):

        self.id_de_vehículo_c = tk.StringVar()
        self.entry_id_de_vehículo= tk.Entry(self,textvariable=self.id_de_vehículo_c)
        self.entry_id_de_vehículo.config(width=20, font=('Arial',12))
        self.entry_id_de_vehículo.grid(row= 1, column=4,padx=10,pady=10, columnspan='2')

        self.id_de_cliente_c = tk.StringVar()
        self.entry_id_de_cliente = tk.Entry(self,textvariable=self.id_de_cliente_c)
        self.entry_id_de_cliente.config(width=20, font=('Arial',12))
        self.entry_id_de_cliente.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.tipo_transaccion_c = tk.StringVar()
        self.entry_tipo_de_transaccion = tk.Entry(self,textvariable=self.tipo_transaccion_c)
        self.entry_tipo_de_transaccion.config(width=20, font=('Arial',12))
        self.entry_tipo_de_transaccion.grid(row= 2, column=4,padx=10,pady=10, columnspan='2')

        self.fecha_c = tk.StringVar()
        self.entry_fecha = tk.Entry(self,textvariable=self.fecha_c)
        self.entry_fecha.config(width=25, font=('Arial',12))
        self.entry_fecha.grid(row= 3, column=1,padx=10,pady=10, columnspan='2')

        self.monto_c = tk.StringVar()
        self.entry_monto = tk.Entry(self,textvariable=self.monto_c)
        self.entry_monto.config(width=15, font=('Arial',12))
        self.entry_monto.grid(row= 3, column=3,padx=10,pady=10, columnspan='4')

        self.observaciones_c = tk.StringVar()
        self.entry_observaciones = tk.Entry(self,textvariable=self.observaciones_c)
        self.entry_observaciones.config(width=50, font=('Arial',12))
        self.entry_observaciones.grid(row= 4, column=1,padx=10,pady=10, columnspan='4')
    
    def tabla_cliente(self):
        self.tabla = ttk.Treeview(self, columns=('ID de Transaccion','ID de Vehículo','ID de Transacción','Fecha','Monto','Observaciones'))
        self.tabla.grid(row=5,column=0,columnspan=6,sticky='nse')

        self.scroll = tk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=5, column=4,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='ID de Transacción (número único y autoincremental)')
        self.tabla.heading('#2',text='ID de Vehículo')
        self.tabla.heading('#3',text='ID de Cliente')
        self.tabla.heading('#4',text='Tipo de Transaccion(compra/Venta)')
        self.tabla.heading('#5',text='Fecha')
        self.tabla.heading('#6',text='Monto')
        self.tabla.heading('#7',text='Observaciones')
