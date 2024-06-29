import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from vistas.claseg import Frame
from controlador.transacciones_dao import leer_transacciones, guardar_transacciones, editar_transacciones, eliminar_transaccion


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
        
        for p in self.contenido_cli:
            self.tabla.insert('',0,text=p['id_transaccion'],
                              values = (p['nombre'],p['apellido'],p['documento'],p['direccion'],p['telefono'],p['correo_electronico']))

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='ID de Transacción (número único y autoincremental)')
        self.tabla.heading('#2',text='ID de Vehículo')
        self.tabla.heading('#3',text='ID de Cliente')
        self.tabla.heading('#4',text='Tipo de Transaccion(compra/Venta)')
        self.tabla.heading('#5',text='Fecha')
        self.tabla.heading('#6',text='Monto')
        self.tabla.heading('#7',text='Observaciones')

        self.tabla.column('#0', width=50)
        self.tabla.column('#1', width=100)
        self.tabla.column('#2', width=100)
        self.tabla.column('#3', width=80)
        self.tabla.column('#4', width=120)
        self.tabla.column('#5', width=80)
        self.tabla.column('#6', width=150)

        self.btn_editar = tk.Button(self, text='Editar', command= self.editar_registro)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar.grid(row= 7, column=0,padx=10,pady=10, columnspan=2)

        self.btn_delete = tk.Button(self, text='Borrar', command= self.borrar_cliente)
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete.grid(row= 7, column=2,padx=10,pady=10, columnspan=2)

        self.buscar_c = tk.StringVar()
        self.buscar_c.set("example@example.com")
        self.entry_buscar = tk.Entry(self,textvariable=self.buscar_c)
        self.entry_buscar.config(width=30, font=('Arial',12))
        self.entry_buscar.grid(row= 7, column=4,padx=10,pady=10, columnspan='2')

        self.btn_buscar = tk.Button(self, text='Buscar', command= self.buscar_registro)
        self.btn_buscar.config(width= 10,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#7B7B78',cursor='hand2',activebackground='#C6C6C0',activeforeground='#FFFFFF')
        self.btn_buscar.grid(row= 7, column=7,padx=10,pady=10)


    def editar_registro(self):
        try:
            self.id_tra = self.tabla.item(self.tabla.selection())['text']

            self.nombre_cliente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellido_cliente = self.tabla.item(self.tabla.selection())['values'][1]
            self.doc_cliente = self.tabla.item(self.tabla.selection())['values'][2]
            self.dir_cliente = self.tabla.item(self.tabla.selection())['values'][3]
            self.mail_cliente = self.tabla.item(self.tabla.selection())['values'][5]
            self.tel_cliente = self.tabla.item(self.tabla.selection())['values'][4]

            self.habilitar_campos()
            self.nombre_c.set(self.nombre_cliente)
            self.apellido_c.set(self.apellido_cliente)
            self.documento_c.set(self.doc_cliente)
            self.direccion_c.set(self.dir_cliente)
            self.telefono_c.set(self.tel_cliente)
            self.correo_c.set(self.mail_cliente)

        except Exception as e:
            messagebox.showerror("Error", f"{e}")

    def guardar_campos(self):
        persona = {
        "id_cliente": '',
        "nombre": self.nombre_c.get(),
        "apellido": self.apellido_c.get(),
        "documento": self.documento_c.get(),
        "direccion":  self.direccion_c.get(),
        "telefono": self.telefono_c.get(),
        "correo_electronico": self.correo_c.get()
    }

        if self.id_transaccion == None:
            guardar_transacciones(persona,'transaccion')
        else:
            editar_transacciones(persona,'transaccion', int(self.id_transaccion))