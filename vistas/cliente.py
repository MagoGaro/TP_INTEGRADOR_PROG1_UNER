import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from .claseg import Frame
from controlador.cliente_dao import leer_cliente, guardar_cliente, editar_cliente, eliminar_cliente


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
        self.id_cli = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.tabla_cliente()

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
        self.entry_nombre.config(width=20, font=('Arial',12),state='disabled')
        self.entry_nombre.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')

        self.apellido_c = tk.StringVar()
        self.entry_apellido = tk.Entry(self,textvariable=self.apellido_c)
        self.entry_apellido.config(width=20, font=('Arial',12),state='disabled')
        self.entry_apellido.grid(row= 1, column=4,padx=10,pady=10, columnspan='2')

        self.documento_c = tk.StringVar()
        self.entry_documento = tk.Entry(self,textvariable=self.documento_c)
        self.entry_documento.config(width=20, font=('Arial',12),state='disabled')
        self.entry_documento.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.telefono_c = tk.StringVar()
        self.entry_telefono = tk.Entry(self,textvariable=self.telefono_c)
        self.entry_telefono.config(width=20, font=('Arial',12),state='disabled')
        self.entry_telefono.grid(row= 2, column=4,padx=10,pady=10, columnspan='2')

        self.direccion_c = tk.StringVar()
        self.entry_direccion = tk.Entry(self,textvariable=self.direccion_c)
        self.entry_direccion.config(width=25, font=('Arial',12),state='disabled')
        self.entry_direccion.grid(row= 3, column=1,padx=10,pady=10, columnspan='4')

        self.correo_c = tk.StringVar()
        self.entry_correo = tk.Entry(self,textvariable=self.correo_c)
        self.entry_correo.config(width=50, font=('Arial',12),state='disabled')
        self.entry_correo.grid(row= 4, column=1,padx=10,pady=10, columnspan='6')
    
    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo',command= self.habilitar_campos)
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_alta.grid(row= 5, column=0,padx=10,pady=10, columnspan='2')

        self.btn_modi = tk.Button(self, text='Guardar',command= self.guardar_campos)
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000',state='disabled')
        self.btn_modi.grid(row= 5, column=2,padx=10,pady=10, columnspan='2')

        self.btn_cance = tk.Button(self, text='Cancelar', command= self.bloquear_campos)
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000',state='disabled')
        self.btn_cance.grid(row= 5, column=4,padx=10,pady=10, columnspan='2')

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_documento.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_direccion.config(state='normal')
        self.entry_correo.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_documento.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_direccion.config(state='disabled')
        self.entry_correo.config(state='disabled')

        self.nombre_c.set('')
        self.apellido_c.set('')
        self.documento_c.set('')
        self.direccion_c.set('')
        self.telefono_c.set('')
        self.correo_c.set('')

        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')

    def tabla_cliente(self):

        self.contenido_cli = leer_cliente('clientes')
        self.contenido_cli.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre','Apellido','Documento','Direccion','Telefono','Correo Electronico'))
        self.tabla.grid(row=6,column=0,columnspan=6,sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=6,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        for p in self.contenido_cli:
            self.tabla.insert('',0,text=p['id_cliente'],
                              values = (p['nombre'],p['apellido'],p['documento'],p['direccion'],p['telefono'],p['correo_electronico']))

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Apellido')
        self.tabla.heading('#3',text='Documento')
        self.tabla.heading('#4',text='Direccion')
        self.tabla.heading('#5',text='Telefono')
        self.tabla.heading('#6',text='Correo Electronico')

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

    def editar_registro(self):
        try:
            self.id_cli = self.tabla.item(self.tabla.selection())['text']

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

        if self.id_cli == None:
            guardar_cliente(persona,'clientes')
        else:
            editar_cliente(persona,'clientes', int(self.id_cli))

        self.id_cli = None
        self.tabla_cliente()
        self.bloquear_campos()
    
    def borrar_cliente(self):
        try:
            response = messagebox.askyesno("Confirmar acción", "¿Desea eliminar al Cliente?")
            if response:
                eliminar_cliente('clientes', int(self.tabla.item(self.tabla.selection())['text']))
                self.tabla_cliente()
        except Exception as e:
            messagebox.showerror("Error", f"{e}")







