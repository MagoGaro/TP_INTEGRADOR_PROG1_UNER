import tkinter as tk
from vistas.claseg import Frame


def open_vista_creadores(root):
    vista_creadores = tk.Toplevel(root)
    vista_creadores.title('Gestor Autos - Creadores')
    vista_creadores.iconbitmap('img/autito.ico')
    vista_creadores.resizable(0,0)

    app = Frame6(root = vista_creadores)


class Frame6(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.ver_creadores()

    def ver_creadores(self):
        self.label_titulo_creadores= tk.Label(self,text= 'Creadores')
        self.label_titulo_creadores.config(font=('Arial',20,'bold'))
        self.label_titulo_creadores.grid(row= 0, column=3,padx=10,pady=10)

        self.label_titulo_creadores2= tk.Label(self,text= 'Nombre')
        self.label_titulo_creadores2.config(font=('Arial',15,'bold'))
        self.label_titulo_creadores2.grid(row= 1, column=2,padx=10,pady=10)

        self.label_titulo_creadores3= tk.Label(self,text= 'Contacto')
        self.label_titulo_creadores3.config(font=('Arial',15,'bold'))
        self.label_titulo_creadores3.grid(row= 1, column=4,padx=10,pady=10)

        self.label_name_creadores= tk.Label(self,text= 'Maria Julieta Gutierrez',fg="#FF5733")
        self.label_name_creadores.config(font=('Arial',12,'bold'))
        self.label_name_creadores.grid(row= 2, column=2,padx=10,pady=10)

        self.label_name_creadores2= tk.Label(self,text= 'Mayra Sofia Rossetto Barcala',fg='#CF93FF')
        self.label_name_creadores2.config(font=('Arial',12,'bold'))
        self.label_name_creadores2.grid(row= 3, column=2,padx=10,pady=10)

        self.label_name_creadores3= tk.Label(self,text= 'María Belén Rabel Zárate',fg='#4EB0EC')
        self.label_name_creadores3.config(font=('Arial',12,'bold'))
        self.label_name_creadores3.grid(row= 4, column=2,padx=10,pady=10)

        self.label_name_creadores4= tk.Label(self,text= 'Gabriel Sebastian Roman',fg='#2F3189')
        self.label_name_creadores4.config(font=('Arial',12,'bold'))
        self.label_name_creadores4.grid(row= 5, column=2,padx=10,pady=10)

        self.label_correo_creadores= tk.Label(self,text= 'julimaxizoe@gmail.com',fg="#FF5733")
        self.label_correo_creadores.config(font=('Arial',12,'bold'))
        self.label_correo_creadores.grid(row= 2, column=4,padx=10,pady=10)

        self.label_correo_creadores2= tk.Label(self,text= 'mrossetto.b@gmail.com',fg='#CF93FF')
        self.label_correo_creadores2.config(font=('Arial',12,'bold'))
        self.label_correo_creadores2.grid(row= 3, column=4,padx=10,pady=10)

        self.label_correo_creadores3= tk.Label(self,text= 'belenrabel03@gmail.com',fg='#4EB0EC')
        self.label_correo_creadores3.config(font=('Arial',12,'bold'))
        self.label_correo_creadores3.grid(row= 4, column=4,padx=10,pady=10)

        self.label_correo_creadores4= tk.Label(self,text= 'gabriel.magogaro@gmail.com',fg='#2F3189')
        self.label_correo_creadores4.config(font=('Arial',12,'bold'))
        self.label_correo_creadores4.grid(row= 5, column=4,padx=10,pady=10)