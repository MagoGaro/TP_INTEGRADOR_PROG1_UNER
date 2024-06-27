import tkinter as tk
from tkinter import ttk

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=480,height=320)
        self.root = root
        self.pack()

    def label_form(self):
        pass
    
    def input_form(self):
        #aca limpiamos la lista de tuplas que nos retorna la funcion
      

        #concatenemos el nuevo array
        self.generos = ['Seleccione uno']
        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero['values'] = self.generos
        self.entry_genero.current(0)
        self.entry_genero.config(width=25, state='disabled',font=('Arial',12))
        self.entry_genero.bind("<<ComboboxSelected>>")
        self.entry_genero.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

    def botones_principales(self):
        pass

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_genero.current(0)
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.nombre.set('')
        self.duracion.set('')
        self.id_peli = None #reseteanis el id luego de eliminar
        self.btn_alta.config(state='normal')

    def guardar_campos(self):
        pelicula = Peliculas(
            self.nombre.get(),
            self.duracion.get(),
            self.entry_genero.current()
        )

        if self.id_peli == None:
            guardar_peli(pelicula)
        else:
            editar_peli(pelicula, int(self.id_peli))

        self.mostrar_tabla()
        self.bloquear_campos()

    def mostrar_tabla(self):
        self.lista_p = listar_peliculas()
        #print(listar_peliculas())
        self.lista_p.reverse() #para invertir el orden
        self.tabla = ttk.Treeview(self, columns=('Nombre','Duración','Genero'))
        self.tabla.grid(row=4,column=0,columnspan=4,sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Duración')
        self.tabla.heading('#3',text='Genero')
       
        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0],
                              values = (p[1],p[2],p[5]))
       
        self.btn_editar = tk.Button(self, text='Editar',command=self.editar_registro)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar.grid(row= 5, column=0,padx=10,pady=10)

        self.btn_delete = tk.Button(self, text='Borrar', command=self.eliminar_registro)
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete.grid(row= 5, column=1,padx=10,pady=10)

    def editar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']

            self.nombre_peli_e = self.tabla.item(self.tabla.selection())['values'][0]
            self.dura_peli_e = self.tabla.item(self.tabla.selection())['values'][1]
            self.gene_peli_e = self.tabla.item(self.tabla.selection())['values'][2]

            self.habilitar_campos()
            self.nombre.set(self.nombre_peli_e)
            self.duracion.set(self.dura_peli_e)
            self.entry_genero.current(self.generos.index(self.gene_peli_e))

        except:
            pass
    
    def eliminar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']
            borrar_peli(int(self.id_peli))
            self.mostrar_tabla()
            self.id_peli = None #reseteanis el id luego de eliminar
        except:
            pass