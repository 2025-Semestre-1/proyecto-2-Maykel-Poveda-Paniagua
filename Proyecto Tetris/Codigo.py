import tkinter as tk
import random
from PIL import Image, ImageTk

# Configuracion del juego
FONDO_DEL_TABLERO = "Dark slate gray"
ANCHO = 12
ALTURA = 22
TAMANO_CELDA = 30

# Ventana de principal
principal = tk.Tk()
principal.geometry("600x600+370+65")
principal.resizable(False,False)
principal.title("Tetris")
principal.iconbitmap("Proyecto Tetris/ra.ico")

##############################################################################################################

# Frames Contenedor
contenedor_Principal = tk.LabelFrame(principal, bd=10, bg=FONDO_DEL_TABLERO)
contenedor_Principal.configure(width=600, height=600)
contenedor_Principal.pack()

# Frame del Juego
frame_Juego = tk.LabelFrame(contenedor_Principal, bd= 10, bg=FONDO_DEL_TABLERO)
frame_Juego.configure(width=350, height=600, bg=FONDO_DEL_TABLERO)
frame_Juego.pack(side="left")






# Frame de Opciones
frame_Opciones = tk.Frame(contenedor_Principal)
frame_Opciones.configure(width=250, height=600)
frame_Opciones.pack(side="right")

# Frame de Opciones de Estadistica
frame_Opc_Estadistica = tk.LabelFrame(frame_Opciones, text="ESTADISTICA", bd=10, bg=FONDO_DEL_TABLERO,
                                      font=("Helvetica", 10, "bold"), fg="white", labelanchor="n")
frame_Opc_Estadistica.configure(width=250, height=250)
frame_Opc_Estadistica.pack(side="top")

# Etiquetas de estadísticas dentro del frame de estadística
lbl_puntaje = tk.Label(frame_Opc_Estadistica, text="Puntaje: 0", bg="gray77", font=("Helvetica", 11, "bold"))
lbl_puntaje.pack(pady=30)

lbl_lineas = tk.Label(frame_Opc_Estadistica, text="Líneas: 0", bg="gray77", font=("Helvetica", 11, "bold"))
lbl_lineas.pack(pady=5)

lbl_piezas = tk.Label(frame_Opc_Estadistica, text="Piezas: 0", bg="gray77", font=("Helvetica", 11, "bold"))
lbl_piezas.pack(pady=5)
frame_Opc_Estadistica.pack_propagate(False)



# Frame de Opciones de Juego
frame_Opc_Juego = tk.LabelFrame(frame_Opciones, text="OPCIONES DE JUEGO", bd=10, bg=FONDO_DEL_TABLERO,
                                font=("Helvetica", 10, "bold"), fg="white", labelanchor="n")
frame_Opc_Juego.configure(width=250, height=350)
frame_Opc_Juego.pack(side="bottom")

# Botones en el panel de juego
btn_iniciar = tk.Button(frame_Opc_Juego, text="Iniciar Juego", width=20, command=lambda: print("Iniciar"))
btn_iniciar.pack(pady=30)

btn_guardar = tk.Button(frame_Opc_Juego, text="Guardar Juego", width=20, command=lambda: print("Guardar"))
btn_guardar.pack(pady=5)

btn_cargar = tk.Button(frame_Opc_Juego, text="Cargar Juego", width=20, command=lambda: print("Cargar"))
btn_cargar.pack(pady=5)

btn_ranking = tk.Button(frame_Opc_Juego, text="Ver Ranking", width=20, command=lambda: print("Ranking"))
btn_ranking.pack(pady=5)

btn_salir = tk.Button(frame_Opc_Juego, text="Salir", width=20, command=principal.quit)
btn_salir.pack(pady=30)
frame_Opc_Juego.pack_propagate(False)

##############################################################################################################

# Diccionario de colores para los tetrominos
COLORES_TETRIS = {"O": "yellow",
               "I": "cyan",
               "L": "orange",
               "J": "blue",
               "T": "purple",
               "Z": "red",
               "U": "green",
               "+": "pink"
        }


principal.mainloop()