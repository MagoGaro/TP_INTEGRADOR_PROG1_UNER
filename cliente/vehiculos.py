import tkinter as tk
from vistas.claseg import Frame


def open_vista_vehiculos(root):
    vista_vehiculos = tk.Toplevel(root)
    vista_vehiculos.title('Gestor Autos - Vehiculos')
    vista_vehiculos.iconbitmap('img/autito.ico')
    vista_vehiculos.resizable(0,0)

    # Add widgets to the secondary window here
    app = Frame3(root = vista_vehiculos)

    # Create a button to close the secondary window
    close_button = tk.Button(vista_vehiculos, text="Close", command=vista_vehiculos.destroy)
    close_button.pack()

class Frame3(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()











