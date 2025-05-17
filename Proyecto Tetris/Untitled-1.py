import tkinter as tk
import random
from PIL import Image, ImageTk

# Configuracion del juego
FONDO_DEL_TABLERO = "black"

ANCHO = 12
ALTURA = 22
TAMANO_CELDA = 30

bienvenida = tk.Tk()
bienvenida.geometry("400x600")
bienvenida.resizable(False,False)
imagen = Image.open("R.ico")
icono = ImageTk.PhotoImage(imagen)
bienvenida.iconphoto(True,icono)


bienvenida.mainloop()