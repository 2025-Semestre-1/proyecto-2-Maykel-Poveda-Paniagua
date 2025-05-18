import tkinter as tk
import random
from PIL import Image, ImageTk

###############################################################################################################
# Configuracion y formato del juego
BOTONES_FORMATO = ("Helvetica",10,"bold") 
FONDO_DEL_TABLERO = "Dark slate gray"
ANCHO = 14 
ALTURA = 24
TAMANO_CELDA = 26



###############################################################################################################
# Ventana de principal
principal = tk.Tk()
principal.geometry("650x690+370+3")
principal.resizable(False,False)
principal.title("Tetris")
principal.iconbitmap("Proyecto Tetris/ra.ico")

# Ventana de informacion
ventana_informacion = tk.Toplevel(principal,bg=FONDO_DEL_TABLERO)
ventana_informacion.geometry("200x100+640+270")
ventana_informacion.iconbitmap("Proyecto Tetris/ra.ico")
ventana_informacion.resizable(False,False)

lbl_informacion = tk.Label(ventana_informacion,text="Escribe tu nombre",bg= FONDO_DEL_TABLERO,
                       fg= "white", font= ("Helvetica", 11, "bold")).pack()
entrada_tex = tk.Entry(ventana_informacion,width=20).pack(pady=5)

boton_informacion = tk.Button(ventana_informacion, text="Confirmar", bg= "grey", font=("Helvetica",10,"bold"),fg="white",
                        width=10, height=1, command=lambda: print("Confirmar")).pack(pady=1)

##############################################################################################################

# Frames Contenedor
contenedor_Principal = tk.LabelFrame(principal, bd=10, bg=FONDO_DEL_TABLERO)
contenedor_Principal.configure(width=650, height=690)
contenedor_Principal.pack()
contenedor_Principal.pack_propagate(False)

# Frame del Juego
frame_Juego = tk.LabelFrame(contenedor_Principal, text="JUEGO", bd=10,
                                      font=("Helvetica", 10, "bold"), fg="white", labelanchor="n")
frame_Juego.configure(width=400, height=660, bg=FONDO_DEL_TABLERO)
frame_Juego.pack(side="left")
frame_Juego.pack_propagate(False)

# Canvas donde esta el tablero
canvas_juego = tk.Canvas(frame_Juego, width=ANCHO*TAMANO_CELDA, height=ALTURA*TAMANO_CELDA, bg="black")
canvas_juego.pack()


# Frame de Opciones
frame_Opciones = tk.Frame(contenedor_Principal)
frame_Opciones.configure(width=250, height=660)
frame_Opciones.pack(side="right")

# Frame de Opciones de Estadistica
frame_Opc_Estadistica = tk.LabelFrame(frame_Opciones, text="ESTADISTICA", bd=10, bg=FONDO_DEL_TABLERO,
                                      font=("Helvetica", 10, "bold"), fg="white", labelanchor="n")
frame_Opc_Estadistica.configure(width=250, height=285)
frame_Opc_Estadistica.pack(side="top")

# Etiquetas de estadísticas dentro del frame de estadística
lbl_puntaje = tk.Label(frame_Opc_Estadistica, text="Puntos: 0",bg= FONDO_DEL_TABLERO,
                       fg= "white", font= ("Helvetica", 15, "bold"))
lbl_puntaje.pack(pady=15)

lbl_lineas = tk.Label(frame_Opc_Estadistica, text="Líneas: 0",bg= FONDO_DEL_TABLERO,
                      fg= "white", font= ("Helvetica", 15, "bold"))
lbl_lineas.pack(pady=15)

lbl_piezas = tk.Label(frame_Opc_Estadistica, text="Piezas: 0",bg= FONDO_DEL_TABLERO,
                      fg= "white", font= ("Helvetica", 15, "bold"))
lbl_piezas.pack(pady=15)
frame_Opc_Estadistica.pack_propagate(False)



# Frame de Opciones de Juego
frame_Opc_Juego = tk.LabelFrame(frame_Opciones, text="OPCIONES DE JUEGO", bd=10, bg=FONDO_DEL_TABLERO,
                                font=("Helvetica", 10, "bold"), fg="white", labelanchor="n")
frame_Opc_Juego.configure(width=250, height=375)
frame_Opc_Juego.pack(side="bottom")

# Botones en el panel de opcion de juego
btn_iniciar = tk.Button(frame_Opc_Juego, text="Iniciar Juego", bg= "dark green", font=BOTONES_FORMATO,fg="white",
                        width=20, height=2, command=lambda: print("Iniciar"))
btn_iniciar.pack(pady=40)

btn_ranking = tk.Button(frame_Opc_Juego, text="Ver Ranking", bg= "blue4", font=BOTONES_FORMATO,fg="white",
                        width=20, height=2, command=lambda: print("Ranking"))
btn_ranking.pack(pady=1)

btn_salir = tk.Button(frame_Opc_Juego, text="Salir",bg="red4", font=BOTONES_FORMATO,fg="white",
                       width=20, height=2, command=principal.destroy)
btn_salir.pack(pady=40)
frame_Opc_Juego.pack_propagate(False)

##############################################################################################################
# Colores para los tetrominos
COLORES_TETRIS = ["yellow",  # O
               "cyan",       # I
               "orange",     # L
               "hot pink",   # J
               "purple",     # T
               "green",      # Z
               "deep pink",  # U
               "red"         # +
            ]

# Formas de los tetrominos
FORMAS_TETRIS = [
    [[1,1],
     [1,1]],           # O
    
    [[1,1,1,1]],       # I
    
    [[1,0,0],
     [1,1,1]],         # L
    
    [[0,0,1],
     [1,1,1]],         # J
    
    [[0,1,0],
     [1,1,1]],         # T

    [[1,1,0],
     [0,1,1]],         # Z

    [[1,0,1],
     [1,1,1]],         # U
    
    [[0,1,0],
     [1,1,1],          # +
     [0,1,0]]
]
###############################################################################################################
'''
E:
S: Tablero con "0" y los bordes con "+" 
'''
def crear_tablero():
    tablero = []
    for i in range(ALTURA):
        fila = []
        for j in range(ANCHO):
            if i == 0 or i == ALTURA-1 or j == 0 or j == ANCHO-1:
                fila += ["+"]
            else:
                fila += [0]
        tablero += [fila]
    return tablero


'''
E: Tablero creado
S: Se dibuja el tablero en el canvas de juego 
'''
def dibujar_tablero(tablero):
    canvas_juego.delete("all")  # se limpia el canvas antes de iniar a dibujar el nuevo tablero
    for y in range(ALTURA):
        for x in range(ANCHO):
            celda = tablero[y][x]
            if celda == "+":
                color = "gray"
            else:
                color = "black"
                
            canvas_juego.create_rectangle(x * TAMANO_CELDA, y * TAMANO_CELDA,
                                          (x + 1) * TAMANO_CELDA,
                                          (y + 1) * TAMANO_CELDA,
                                          fill=color, outline="gray25")
                
tablero = crear_tablero()
dibujar_tablero(tablero)
principal.mainloop()