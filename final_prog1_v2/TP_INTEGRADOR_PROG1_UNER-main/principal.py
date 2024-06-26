import tkinter as tk
from vistas.inicio import Frame2, barrita_menu

def main():
    ventana = tk.Tk()
    ventana.title('Gestor Autos')
    ventana.iconbitmap('img/autito.ico')
    ventana.resizable(0,0)

    barrita_menu(ventana)
    app = Frame2(root = ventana)

    ventana.mainloop()

if __name__ == '__main__':
    main()
    