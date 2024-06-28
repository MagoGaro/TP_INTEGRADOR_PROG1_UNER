import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from vistas.claseg import Frame
from controlador.vehiculos_dao import leer_vehiculo, guardar_vehiculo, editar_vehiculo, eliminar_vehiculo



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
        self.id_veh = None

        self.label_form()
        self.input_form()
        self.tabla_vehiculos()
        self.botones_principales()

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
        self.patente_v = tk.StringVar()
        self.entry_patente = tk.Entry(self,textvariable=self.patente_v)
        self.entry_patente.config(width=20, font=('Arial',12),state='disabled')
        self.entry_patente.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')

        self.marca_v = tk.StringVar()
        self.entry_marca = tk.Entry(self,textvariable=self.marca_v)
        self.entry_marca.config(width=20, font=('Arial',12),state='disabled')
        self.entry_marca.grid(row= 1, column=4,padx=10,pady=10, columnspan='2')
        
        self.modelo_v = tk.StringVar()
        self.entry_modelo = tk.Entry(self,textvariable=self.modelo_v)
        self.entry_modelo.config(width=20, font=('Arial',12),state='disabled')
        self.entry_modelo.grid(row= 2, column=4,padx=10,pady=10, columnspan='2')

        self.tipo_v = tk.StringVar()
        self.entry_tipo = tk.Entry(self,textvariable=self.tipo_v)
        self.entry_tipo.config(width=20, font=('Arial',12),state='disabled')
        self.entry_tipo.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.anio_v = tk.StringVar()
        self.entry_anio = tk.Entry(self,textvariable=self.anio_v)
        self.entry_anio.config(width=20, font=('Arial',12),state='disabled')
        self.entry_anio.grid(row= 4, column=1,padx=10,pady=10, columnspan='2')

        self.kilometraje_v = tk.StringVar()
        self.entry_kilometraje = tk.Entry(self,textvariable=self.kilometraje_v)
        self.entry_kilometraje.config(width=20, font=('Arial',12),state='disabled')
        self.entry_kilometraje.grid(row= 4, column=4,padx=10,pady=10, columnspan='4')

        self.precio_compra_v = tk.StringVar()
        self.entry_precio_compra = tk.Entry(self,textvariable=self.precio_compra_v)
        self.entry_precio_compra.config(width=20, font=('Arial',12),state='disabled')
        self.entry_precio_compra.grid(row=6, column=1,padx=10,pady=10, columnspan='2')

        self.precio_venta_v = tk.StringVar()
        self.entry_precio_venta = tk.Entry(self,textvariable=self.precio_venta_v)
        self.entry_precio_venta.config(width=20, font=('Arial',12),state='disabled')
        self.entry_precio_venta.grid(row= 6, column=4,padx=10,pady=10, columnspan='3')

        self.estado_var = tk.StringVar()
        self.entry_estado = ttk.OptionMenu(self, self.estado_var, "Estado", "Disponible", "Reservado", "Vendido")
        self.entry_estado.grid(row=8, column=1, padx=10, pady=10)
    
    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command= self.habilitar_campos)
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_alta.grid(row=9, column=0, padx=(5, 5), pady=5)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000',state='disabled')
        self.btn_modi.grid(row=9, column=2, padx=(5, 5), pady=5)

        self.btn_cance = tk.Button(self, text='Cancelar', command = self.bloquear_campos)
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000',state='disabled')
        self.btn_cance.grid(row=9, column=4, padx=(5, 5), pady=5)
    
    def habilitar_campos(self):
        self.entry_patente.config(state='normal')
        self.entry_marca.config(state='normal')
        self.entry_tipo.config(state='normal')
        self.entry_anio.config(state='normal')
        self.entry_modelo.config(state='normal')
        self.entry_kilometraje.config(state='normal')
        self.entry_precio_compra.config(state='normal')
        self.entry_precio_venta.config(state='normal')
        self.entry_estado.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_patente.config(state='disabled')
        self.entry_marca.config(state='disabled')
        self.entry_tipo.config(state='disabled')
        self.entry_anio.config(state='disabled')
        self.entry_modelo.config(state='disabled')
        self.entry_kilometraje.config(state='disabled')
        self.entry_precio_compra.config(state='disabled')
        self.entry_precio_venta.config(state='disabled')
        self.entry_estado.config(state='disabled')

        self.patente_v.set('')
        self.marca_v.set('')
        self.tipo_v.set('')
        self.anio_v.set('')
        self.modelo_v.set('')
        self.kilometraje_v.set('')
        self.precio_compra_v.set('')
        self.precio_venta_v.set('')
        self.estado_var.set('Disponible')

        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')
      

    def tabla_vehiculos(self):

        self.contenido_veh = leer_vehiculo('vehiculos')
        self.contenido_veh.reverse()


        self.tabla = ttk.Treeview(self, columns=('Nº de Patente','Marca','Tipo','Anio','Modelo','Kilometraje','Precio Compra', 'Precio Venta', 'Estado'))
        self.tabla.grid(row=10, column=0, columnspan=6, sticky='nsew')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=6, sticky='ns')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        for p in self.contenido_veh:
            self.tabla.insert('',0,text=p['id_vehiculo'],
                                values = (p['patente'],p['marca'],p['modelo'],p['tipo'],p['año'],p['kilometraje'],p['precio_compra'],p['precio_venta'],p['estado']))
        
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nº de Patente')
        self.tabla.heading('#2', text='Marca')
        self.tabla.heading('#3', text='Tipo')
        self.tabla.heading('#4', text='Año')
        self.tabla.heading('#5', text='Modelo')
        self.tabla.heading('#6', text='Kilometraje')
        self.tabla.heading('#7', text='Precio Compra')
        self.tabla.heading('#8', text='Precio Venta')
        self.tabla.heading('#9', text='Estado')

        
        self.tabla.column('#0', minwidth=80, width=100)
        self.tabla.column('#1', minwidth=80, width=100)
        self.tabla.column('#2', minwidth=60, width=80)
        self.tabla.column('#3', minwidth=60, width=80)
        self.tabla.column('#4', minwidth=80, width=100)
        self.tabla.column('#5', minwidth=80, width=100)
        self.tabla.column('#6', minwidth=100, width=110)
        self.tabla.column('#7', minwidth=100, width=110)
        self.tabla.column('#8', minwidth=80, width=90)
        self.tabla.column('#9', minwidth=80, width=90)

        self.btn_editar = tk.Button(self, text='Editar', command= self.editar_registro)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
        

        self.btn_delete = tk.Button(self, text='Borrar', command= self.borrar_vehiculos )
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete.grid(row=11, column=3, columnspan=2, padx=10, pady=10)

    def editar_registro(self):
        try:
            selected_item = self.tabla.selection()
            if not selected_item:
                raise Exception("No se ha seleccionado ningún registro")

            self.id_veh = self.tabla.item(selected_item)['text']

            self.patente_veh = self.tabla.item(selected_item)['values'][0]
            self.marca_veh = self.tabla.item(selected_item)['values'][1]
            self.tipo_veh = self.tabla.item(selected_item)['values'][2]
            self.anio_veh = self.tabla.item(selected_item)['values'][3]
            self.modelo_veh = self.tabla.item(selected_item)['values'][4]
            self.kilometraje_veh = self.tabla.item(selected_item)['values'][5]
            self.valor_compra_veh = self.tabla.item(selected_item)['values'][6]
            self.valor_venta_veh = self.tabla.item(selected_item)['values'][7]
            self.estado_veh = self.tabla.item(selected_item)['values'][8]

            self.habilitar_campos()
            self.patente_v.set(self.patente_veh)
            self.marca_v.set(self.marca_veh)
            self.tipo_v.set(self.tipo_veh)
            self.anio_v.set(self.anio_veh)
            self.modelo_v.set(self.modelo_veh)
            self.kilometraje_v.set(self.kilometraje_veh)
            self.precio_compra_v.set(self.valor_compra_veh)
            self.precio_venta_v.set(self.valor_venta_veh)
            self.estado_var.set(self.estado_veh)

        except Exception as e:
            messagebox.showerror("Error", f"Error al editar el vehículo: {e}")

    def guardar_campos(self):
        auto = {
        "id_vehiculo": '',
        "patente": self.patente_v.get(),
        "marca": self.marca_v.get(),
        "modelo": self.modelo_v.get(),
        "tipo": self.tipo_v.get(),
        "año": self.anio_v.get(),
        "kilometraje": self.kilometraje_v.get(),
        "precio_compra": self.precio_compra_v.get(),
        "precio_venta": self.precio_venta_v.get(),
        "estado": self.estado_var.get(),
    }
        if self.id_veh == None:
            guardar_vehiculo(auto, 'vehiculos')
        else:
            editar_vehiculo(auto, 'vehiculos', int(self.id_veh))

        self.id_veh = None
        self.tabla_vehiculos()
        self.bloquear_campos()
    

    def borrar_vehiculos(self):
        try:
            response = messagebox.askyesno("Confirmar accion", "Desea eliminar un vehiculo?")
            if response:
                eliminar_vehiculo('vehiculos', int(self.tabla.item(self.tabla.selection())['text']))
                self.tabla_vehiculos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el vehículo: {e}")


       











