import tkinter as tk
import random
import re
from PIL import Image, ImageTk
import tkinter.messagebox as tm
import time

###############################################################################################################
# Configuracion y formato del juego
BOTONES_FORMATO = ("Lucida Console",12,"bold") 
FONDO_DEL_TABLERO = "Dark slate gray"
ANCHO = 14 
ALTURA = 24
TAMANO_CELDA = 26

###############################################################################################################
# Ventana de principal
principal = tk.Tk()
principal.geometry("650x680+370+3")
principal.resizable(False,False)
principal.title("Tetris")
try:
    principal.iconbitmap("Proyecto Tetris/ra.ico")
except:
    pass

###############################################################################################################
# Ventana de informacion
ventana_informacion = tk.Toplevel(principal,bg="black")
ventana_informacion.geometry("200x100+640+270")
ventana_informacion.resizable(False,False)
try:
    ventana_informacion.iconbitmap("Proyecto Tetris/ra.ico")
except:
    pass

ventana_informacion.grab_set()   # Bloquea la principal hasta que esta se cierre
ventana_informacion.lift() # Se levanta sobre las demas dando prioridad 
ventana_informacion.focus_force() # Le damos todo el foco
ventana_informacion.transient(principal)  # La vincula como hija visual de la principal
'''
E:
S: Destruir ventana principal
'''
def bloquear_cierre():
    principal.destroy()
    
    
# Bloqueamos la para no salirnos X
ventana_informacion.protocol("WM_DELETE_WINDOW", bloquear_cierre)

##################################
# Etiqueta, entrada de tex y boton de ventana info
lbl_informacion = tk.Label(ventana_informacion,text="Escribe tu nombre",bg= "black",
                       fg= "white", font= ("Helvetica", 11, "bold")).pack()
entrada_tex = tk.Entry(ventana_informacion,width=20)
entrada_tex.pack(pady=5)

ventana_informacion.after(150, lambda: entrada_tex.focus_set())  # Le da el foco o sea tiene prioridad el entry despues de 150 milisegundos

boton_informacion = tk.Button(ventana_informacion, text="Confirmar", bg= "grey", font=("Helvetica",10,"bold"),fg="white",
                        width=10, height=1, command=lambda: obtener_tex())
boton_informacion.pack(pady=1)
boton_informacion.configure(cursor="hand2")

##############################################################################################################
# Frames Contenedor
contenedor_Principal = tk.LabelFrame(principal, bd=10, bg="gold")
contenedor_Principal.configure(width=650, height=680)
contenedor_Principal.pack()
contenedor_Principal.pack_propagate(False)

##############################################################################################################
# Frame del Juego
frame_Juego = tk.LabelFrame(contenedor_Principal, bd=10,
                                      font=("Helvetica", 10, "bold"), fg="white", labelanchor="n")
frame_Juego.configure(width=400, height=660, bg="khaki3")
frame_Juego.pack(side="left")
frame_Juego.pack_propagate(False)

##################################
# Canvas donde esta el tablero
canvas_juego = tk.Canvas(frame_Juego, width=ANCHO*TAMANO_CELDA, height=ALTURA*TAMANO_CELDA,bd=20,bg="black",highlightthickness=0)
canvas_juego.pack(pady=7,padx=7)

##############################################################################################################
# Frame de Opciones
frame_Opciones = tk.Frame(contenedor_Principal)
frame_Opciones.configure(width=250, height=660)
frame_Opciones.pack(side="right")

##################################
# Frame de Opciones de Estadistica
frame_Opc_Estadistica = tk.LabelFrame(frame_Opciones, bd=10, bg="khaki3",
                                      font=("Helvetica", 10, "bold"), fg="white", labelanchor="n")
frame_Opc_Estadistica.configure(width=250, height=285)
frame_Opc_Estadistica.pack(side="top")
frame_Opc_Estadistica.pack_propagate(False)

# Imagen de fondo
imagen_fondo_estadistica = Image.open("Proyecto Tetris/fondo1.png")  # Ruta imagen
imagen_fondo_estadistica = imagen_fondo_estadistica.resize((240, 315), Image.Resampling.LANCZOS)
canvas_Estadistica_es = ImageTk.PhotoImage(imagen_fondo_estadistica)

# Canvas que alberga la imagen
canvas_Estadistica = tk.Canvas(frame_Opc_Estadistica, width=240, height=355, highlightthickness=0)
canvas_Estadistica.pack_propagate(False)
canvas_Estadistica.pack()

# Crea la imagen en el canvas
canvas_Estadistica.create_image(0, 0, anchor="nw", image=canvas_Estadistica_es) # Esquina superior izquierda
canvas_Estadistica.image = canvas_Estadistica_es  # Para que no se elimine la imagen

##################################
# simula pantalla para nombre
frame_pantalla = tk.LabelFrame(canvas_Estadistica,bd=8,bg="gold")
frame_pantalla.pack(pady=12)

# Etiquetas de estadísticas dentro del frame de estadística
Ibl_usuario = tk.Label(frame_pantalla,text="Jugador: ", bg="black",
                        fg="white",bd=7, font=("Helvetica", 15, "bold"))
Ibl_usuario.pack(pady=1)

# Simula pantalla estadistic
frame_para_estadisticas = tk.LabelFrame(canvas_Estadistica,bd=15,bg="gold")
frame_para_estadisticas.configure(width=190, height=160)
frame_para_estadisticas.pack(side="top")
frame_para_estadisticas.pack_propagate(False)

# simula pantalla sin borde dentro de pantalla estaditic
frame_dentro_pantalla = tk.Frame(frame_para_estadisticas,bg="black")
frame_dentro_pantalla.configure(width=190, height=160)
frame_dentro_pantalla.pack_propagate(False)
frame_dentro_pantalla.pack()

####### Esta etiqueta sirve para alinear las otras etiquetas #######
lbl_nada = tk.Label(frame_dentro_pantalla,bg="black",
                        fg= "black", font= ("Courier New", 1, "bold"))
lbl_nada.pack(pady=0)
#######------------------------------------------------------#######

lbl_puntaje = tk.Label(frame_dentro_pantalla, text="Puntos: 0",bg= "black",
                        fg= "white", font= ("Courier New", 13, "bold"))
lbl_puntaje.pack(pady=6)

lbl_lineas = tk.Label(frame_dentro_pantalla, text="Lineas: 0",bg= "black",
                        fg= "white", font= ("Courier New", 13, "bold"))
lbl_lineas.pack(pady=6)

lbl_piezas = tk.Label(frame_dentro_pantalla, text="Piezas: 0",bg= "black",
                        fg= "white", font= ("Courier New", 13, "bold"))
lbl_piezas.pack(pady=6)

##############################################################################################################
# Frame de Opciones de Juego
frame_Opc_Juego = tk.LabelFrame(frame_Opciones, bd=10, bg="khaki3",
                                font=("Helvetica", 10, "bold"), fg="white", labelanchor="n")
frame_Opc_Juego.configure(width=250, height=375)
frame_Opc_Juego.pack(side="bottom")
frame_Opc_Juego.pack_propagate(False)

# Canvas que alberga la imagen
canvas_opciones = tk.Canvas(frame_Opc_Juego, width=230, height=355, highlightthickness=0)
canvas_opciones.pack()

##################################
# Cargar imagen de fondo
imagen_fondo_juego = Image.open("Proyecto Tetris/fondo1.png")  # Cambia al nombre real
imagen_fondo_juego = imagen_fondo_juego.resize((230, 357), Image.Resampling.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen_fondo_juego)

# Crea la imagen en el canvas
canvas_opciones.create_image(0, 0, anchor="nw", image=imagen_tk)
canvas_opciones.image = imagen_tk  # Para que no se elimine la imagen

# Botones en el panel de opcion de juego
btn_iniciar = tk.Button(canvas_opciones, text="Jugar", bg= "dark green", font=BOTONES_FORMATO, fg="white",
                        width=9, height=2, relief="raised", activeforeground="white", activebackground="dark green",
                        bd=10, command=lambda: iniciar())
canvas_opciones.create_window(105, 85, window=btn_iniciar)  # Posición centrada arriba del canvas y la imagen
btn_iniciar.configure(cursor="hand2")

btn_ranking = tk.Button(canvas_opciones, text="Ranking", bg="blue4", font=BOTONES_FORMATO, fg="white",
                        width=9, height=2, relief="raised", activeforeground="white", activebackground="blue4",
                        bd=10, command=lambda: ventana_ranking())

canvas_opciones.create_window(105, 176, window=btn_ranking) # Posición centrada arriba del canvas y la imagen
btn_ranking.configure(cursor="hand2")

btn_salir = tk.Button(canvas_opciones, text="Salir",bg="red4", font=BOTONES_FORMATO,fg="white",
                       width=9, height=2,relief="raised",activeforeground="white",activebackground="red4",
                       bd=10, command=principal.destroy)

canvas_opciones.create_window(105, 270, window=btn_salir) # Posición centrada arriba del canvas y la imagen
btn_salir.configure(cursor="hand2")

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
S: Genera la ventana al tocar el boton de ranking
R: 
'''
def ventana_ranking():

    # Ventana que muestra el Ranking
    Ven_ranking = tk.Toplevel(principal,bg="khaki3") 
    Ven_ranking.title("Ranking")
    Ven_ranking.geometry("500x500+440+100")
    Ven_ranking.resizable(False,False)
    Ven_ranking.grab_set()
    Ven_ranking.focus_set()
    Ven_ranking.transient(principal)
    
    try:
        Ven_ranking.iconbitmap("Proyecto Tetris/ra.ico")
    except:
        pass
    
    # Imagen 
    imagen_fondo_Ranking = Image.open("Proyecto Tetris/fondo1.png")  # Ruta imagen
    imagen_fondo_Ranking = imagen_fondo_Ranking.resize((550, 500), Image.Resampling.LANCZOS)
    canvas_rank = ImageTk.PhotoImage(imagen_fondo_Ranking)
    
    frame_para_ran = tk.LabelFrame(Ven_ranking,bd=15,bg="khaki3")
    frame_para_ran.configure(width=550, height=550)
    frame_para_ran.pack()
    frame_para_ran.pack_propagate(False)
    
    canvas_ran = tk.Canvas(frame_para_ran, width=550, height=550,highlightthickness=0)
    canvas_ran.pack_propagate(False)
    canvas_ran.pack()
    
    canvas_ran.create_image(0, 0, anchor="nw", image=canvas_rank) # Esquina superior izquierda
    canvas_ran.image = canvas_rank  # Para que no se elimine la imagen
    
    # Frame de texto
    frame_ra_panta = tk.LabelFrame(canvas_ran,bg="gold",bd=10)
    frame_ra_panta.pack(fill="both",padx=20, pady=10)
    
    fram_pan = tk.Frame(frame_ra_panta,bg="black",width=430,height=40)
    fram_pan.pack_propagate(False)
    fram_pan.pack()
    
    # Etiqueta de frame de texto
    tk.Label(fram_pan, text="TOP 10 PUNTAJES", font=("Courier New", 16, "bold"), 
             bg="black", fg="white").pack(pady=10)
    
    # Frame de todas las etiquetas
    frame_Ranking = tk.LabelFrame(canvas_ran, bg="gold",bd=10,width=425,height=440)
    frame_Ranking.pack_propagate(False)
    frame_Ranking.pack(fill="both", padx=20, pady=5)
    
    fram_p = tk.Frame(frame_Ranking, bg="black")
    fram_p.pack(fill="both", expand=True)
    
    # Etiquetas
    tk.Label(fram_p, text="Posicion", font=("Courier New", 12, "bold"), 
             bg="black", fg="white", width=13).grid(row=0, column=0)
    tk.Label(fram_p, text="Jugador", font=("Courier New", 12, "bold"), 
             bg="black", fg="white", width=15).grid(row=0, column=1)
    tk.Label(fram_p, text="Puntos", font=("Courier New", 12, "bold"), 
             bg="black", fg="white", width=10).grid(row=0, column=2)
    
    try:
        with open("Proyecto Tetris/Ranking.txt","r") as archi:
        
            lineas = archi.readlines()
        
        datos = []
        for linea in lineas:
            partes = linea.strip().split(",")
            
            if len(partes) == 2:
                nom = partes[0]
                puntos = int(partes[1])
                
                datos += [[nom,puntos]]
    except:
        pass # Caso de que no tenga nada el archivo
    
    tama_lista = len(datos)
    for _ in range(tama_lista):
        for i in range(tama_lista - 1):
            if datos[i][1] < datos[i + 1][1]:
                # Se dan vuelta entre los dos
                temporal = datos[i]
                datos[i] = datos[i + 1]
                datos[i + 1] = temporal
                
    for i in range(min(10,len(datos))):
        tk.Label(fram_p, text=str(i+1), font=("Courier New", 12, "bold"), 
            bg="black", fg="white", width=13).grid(row=i+1, column=0)
        tk.Label(fram_p, text=datos[i][0], font=("Courier New", 12, "bold"), 
            bg="black", fg="white", width=15).grid(row=i+1, column=1)
        tk.Label(fram_p, text=datos[i][1], font=("Courier New", 12, "bold"), 
            bg="black", fg="white", width=10).grid(row=i+1, column=2)
            
 
#---------------------------------------------------------------------------------#
#                             Funciones del Juego                                 #
#---------------------------------------------------------------------------------#

'''
E: Nombre proporcionado por el usuario
S: El nombre con sus respectivas estadisticas
R: No debe tener numeros ni estar vacio
'''
def obtener_tex():
    nombre = entrada_tex.get()
   
    if nombre.strip() == "":
        tm.showerror("Texto Invalido", "El nombre no puede estar vacio.")
        return
        
    if not re.match(r"^[a-zA-Z\s]+$", nombre):
        tm.showerror("Texto Invalido", "El nombre debe de contener solo letras.")
        return
    
    elif len(nombre) > 11:
        tm.showerror("Texto Invalido", "El nombre no debe pasar de 11 caracteres.")
        return
    
    Ibl_usuario.configure(text=f"Jugador: {nombre}")
    global nombre_jugador
    
    nombre_jugador = nombre
    ventana_informacion.destroy()
    time.sleep(0.5)
    tm.showinfo("Información","Si deseas agregar obstaculos has click en las casillas")
    return nombre

def actualizar_estadisticas():
    if juego_en_proceso:
        lbl_puntaje.config(text=f"Puntos: {puntaje_actual}")
        lbl_lineas.config(text=f"Lineas: {lineas_totales}")
        lbl_piezas.config(text=f"Piezas: {piezas_colocadas}")

juego_en_proceso = False

'''
E:
S: Tablero con "0" y los bordes con "+" 
'''
def crear_matriz():
    with open("Proyecto Tetris/Matriz.txt","w") as archivo:
        for i in range(ALTURA):
            fila = ""
            for j in range(ANCHO):
                if i == 0 or i == ALTURA-1 or j == 0 or j == ANCHO-1:
                    fila += "+" + " "
                else:
                    fila += "0" + " "
            archivo.write(fila.strip()+ "\n")

'''
E:
S: Diccionario con su respectiva forma, color y cordenadas
'''   
def crear_pieza():
    indice = random.randint(0, 7)
    forma = FORMAS_TETRIS[indice]
    color = COLORES_TETRIS[indice]
    if indice == 1:
        x = 5
        y = 1
    else:
        x = 6
        y = 1
        
    return {"forma": forma, "color": color, "x": x, "y": y}  # Diccionario

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
                
            elif celda == "#":
                color = "gray"
                
            elif celda == "0":
                color = "black"
                
            else:
                color = celda   # Color de las piezas                 
            canvas_juego.create_rectangle(x * TAMANO_CELDA, y * TAMANO_CELDA,
                                            (x + 1) * TAMANO_CELDA,
                                            (y + 1) * TAMANO_CELDA,
                                            fill=color, outline="gray")   
'''
E: 
S: Extrae la matriz del archivo txt 
'''
def extraerMatriz():
    with open("Proyecto Tetris/Matriz.txt", "r") as archi:
        lineas = archi.readlines()
        matriz = []
            
        for linea in lineas:
            fila = linea.strip().split()
            matriz += [fila]

        return matriz

'''
E: Evento "click"
S: Dibuja obstaculos en el canvas
'''
def click_canva(evento):
    if juego_en_proceso:
        return
    
    x = evento.x // TAMANO_CELDA
    y = evento.y // TAMANO_CELDA
    
    if 0 <= x < ANCHO and 0 <= y < ALTURA:
        with open("Proyecto Tetris/Matriz.txt", "r") as archivo:
            lineas = archivo.readlines()
            
            matriz = []
            for linea in lineas:
                fila = linea.strip().split()
                matriz += [fila]
                
            if matriz[y][x] != "+":
                if matriz[y][x] == "0":
                    matriz[y][x] = "#"
                    
                else:
                    matriz[y][x] = "0"
            
            with open("Proyecto Tetris/Matriz.txt", "w") as archivo:
                for fila in matriz:
                    fila_txt = ""
                    for cuadro in fila:
                        fila_txt += cuadro + " "
                    archivo.write(fila_txt.strip() + "\n")
                        
            dibujar_tablero(matriz)        


###############################################
#         Apartado Global
###############################################  

# Instruccion para poder agregar obtaculos           
canvas_juego.bind("<Button-1>", click_canva)
# Bandera para bloquea click
juego_en_proceso = False
# Variable que contiene la extraccion de matriz
tablero = extraerMatriz()
# Se dibuja el tablero para que el usuario se guie para poner obtaculos
dibujar_tablero(tablero)

###############################################

'''
E: Diccionario con los parametros de cada figura
S: Pieza dibujada en el canvas
'''   
def dibujar_pieza(pieza):
    forma = pieza["forma"]
    color = pieza["color"]
    x_posicion = pieza["x"]
    y_posicion = pieza["y"]

    y_local = 0   # Lleva el control de las filas
    for fila in forma:  # Recorre la forma
        x_local = 0   # Lleva el control de las columnas
        for bloque in fila:  # Recorre los bloques
            if bloque == 1:
                x_canvas = (x_local + x_posicion) * TAMANO_CELDA
                y_canvas = (y_local + y_posicion) * TAMANO_CELDA
                
                canvas_juego.create_rectangle(
                                x_canvas, y_canvas,
                                x_canvas + TAMANO_CELDA, y_canvas + TAMANO_CELDA,
                                fill=color, outline="black", width=2
                )
            x_local += 1
        y_local += 1

'''
E: Tablero extraido del archivo txt y pieza con los parametros del diccionario
S: Actualiza el tablero para mostrar los cambios dados
'''          
def actualizar_canvas(tablero, pieza):
    canvas_juego.delete("all")
    dibujar_tablero(tablero) # Se dibuja el tablero despues de 0 milisegundos
    dibujar_pieza(pieza) # Se dibuja la pieza despues de 500 milisegundos

'''
E: Tablero extraido del archivo txt y pieza con los parametros del diccionario
S: Valor booleano que verifica si hay o no colision
'''   
def colision(pieza,tablero):
    forma = pieza["forma"]
    x = pieza["x"]
    y = pieza["y"]

    y_local = 0   # Lleva el control de las filas
    for fila in forma:  # Recorre la forma
        x_local = 0   # Lleva el control de las columnas
        for bloque in fila:  # Recorre los bloques
            if bloque == 1:
                tablero_x = x_local + x
                tablero_y = y_local + y
                
                if 0 <= tablero_x < ANCHO and 0 <= tablero_y < ALTURA:
                    if tablero[tablero_y][tablero_x] != "0":
                        return True               
                else:
                    return True
                
            x_local += 1
        y_local += 1
            
    return False

'''
E: Pieza que el diccionario, la extracion del la matriz en txt, y las cordenadas a cambiar
S: Pieza con nuevos parametros de ubicacion
'''   
def mover(pieza, dx, dy, tablero):
    nuevo_y = pieza["y"] + dy
    nuevo_x = pieza["x"] + dx
    
    # Diccionario que simula el movimiento
    nueva_pieza = {
        "forma": pieza["forma"],
        "color": pieza["color"],
        "y": nuevo_y,
        "x": nuevo_x
    }
    
    if not colision(nueva_pieza,tablero):
        pieza["x"] = nuevo_x
        pieza["y"] = nuevo_y
        actualizar_canvas(tablero, pieza)
        return True
    else:
        return False
        
'''
E: Pieza del diccionario y la extracion del la matriz en txt
S: Pieza rotada 
'''          
def rotar_pieza(pieza, tablero):
    if pieza["color"] == "yellow":
        return
    if pieza["color"] == "red":
        return
    
    pieza_nueva = pieza["forma"]
    
    filas = len(pieza_nueva)
    columnas = len(pieza_nueva[0])
    
    matriz = []
    for x in range(columnas):
        fila_rotada = []
        for y in range(filas -1, -1, -1):
            fila_rotada += [pieza_nueva[y][x]]
        matriz += [fila_rotada]
        
    # Diccionario que simula el movimiento
    Nueva_rotar = {
        "forma": matriz,
        "color": pieza["color"],
        "x": pieza["x"],
        "y": pieza["y"]
    }
    
    if not colision(Nueva_rotar,tablero):
        pieza["forma"] = matriz
        actualizar_canvas(tablero, pieza)

'''
E: Pieza del diccionario y la extracion del la matriz en txt
S: Pieza fijada
'''  
def fijar_pieza(pieza,tablero):
    forma = pieza["forma"]
    x_local = pieza["x"]
    y_local = pieza["y"]
    
    fila = len(forma)
    columna = len(forma[0])
    
    for y in range(fila):
        for x in range(columna):
            if forma[y][x] == 1:
                tablero_x = x_local + x
                tablero_y = y_local + y
                
                if 0 < tablero_y < ALTURA-1 and 0 < tablero_x < ANCHO-1:
                    tablero[tablero_y][tablero_x] = pieza["color"]
                    
'''
E: La extracion del la matriz en txt
S: Elimina lineas con un mismo valor
''' 
def eliminar_lineas(tablero):
    lineas_eliminadas = 0

    # Recorre desde abajo hacia arriba
    for y in range(ALTURA - 2, 0, -1):
        es_completa = True
        
        for x in range(1, ANCHO - 1):
            if tablero[y][x] == "0" or tablero[y][x] == "#":
                es_completa = False
                break

        if es_completa:
            # Elimina la línea
            for x in range(1, ANCHO - 1):
                tablero[y][x] = "0"

            for fila in range(y, 1, -1):  # desde y hasta la fila 2
                
                for col in range(1, ANCHO - 1):
        
                    if tablero[fila][col] != "#" and tablero[fila - 1][col] != "#":
                        tablero[fila][col] = tablero[fila - 1][col]
                    elif tablero[fila - 1][col] == "#":
                        tablero[fila][col] = "0"  # Si lo de arriba era obstaculo no se copia

            # Limpia la fila 1
            for x in range(1, ANCHO - 1):
                if tablero[1][x] != "#":
                    tablero[1][x] = "0"

            lineas_eliminadas += 1
            y += 1  # Vuelve a verificar la misma fila

    return lineas_eliminadas

def guardar_puntaje():
    with open("Proyecto Tetris/Ranking.txt", "a") as archivo:
        archivo.write(f"{nombre_jugador},{puntaje_actual}\n")

#############################################
#                  Juego 
#############################################
'''
E: 
S: Bucle del juego
'''
def iniciar():
    global juego_en_proceso, pieza_actual, tablero, puntaje_actual, lineas_totales, piezas_colocadas
    juego_en_proceso = True
    
    lbl_puntaje.config(text=f"Puntos: 0")
    lbl_lineas.config(text=f"Lineas: 0")
    lbl_piezas.config(text=f"Piezas: 0")
    
    puntaje_actual = 0
    lineas_totales = 0
    piezas_colocadas = 0

    tablero = extraerMatriz() # Variable que contiene la matriz actualizada
    pieza_actual = crear_pieza() # Variable que tiene la pieza base
    actualizar_canvas(tablero, pieza_actual)
    
    '''
    E: Evento
    S: Pieza movida a la derecha
    ''' 
    def derecha(e):
        mover(pieza_actual,1,0,tablero)
        
    '''
    E: Evento
    S: Pieza movida a la izquierda
    '''         
    def izquierda(e):
        mover(pieza_actual,-1,0,tablero)

    '''
    E: Evento
    S: Pieza rotada
    '''        
    def rotar(e):
        rotar_pieza(pieza_actual, tablero)
    
    '''
    E: Evento
    S: Pieza movida hacia abajo
    ''' 
    def abajo(e):
        mover(pieza_actual,0,1,tablero)
    
    '''
    E: 
    S: Bucle del juego para hasta que se pierda 
    '''         
    def bucle_del_juego():
        global pieza_actual, juego_en_proceso, puntaje_actual, lineas_totales, piezas_colocadas
        
        if not mover(pieza_actual, 0, 1, tablero):
            fijar_pieza(pieza_actual, tablero)
            lineas = eliminar_lineas(tablero)

            puntaje_actual += lineas * 100
            lineas_totales += lineas
            piezas_colocadas += 1
            actualizar_estadisticas()
            
            pieza_actual = crear_pieza()
            
            if colision(pieza_actual, tablero): # Se pregunta si coliciona al aparecer
                guardar_puntaje()

                tm.showinfo("Game Over","Has perdido, inténtalo de nuevo")
                juego_en_proceso = False
                
                return  # Detiene el bucle
            
        canvas_juego.after(1000, bucle_del_juego)
        
    canvas_juego.focus_set() # Se le da el foco al canva
    
    canvas_juego.bind("<Left>", izquierda) 
    canvas_juego.bind("<Right>", derecha) 
    canvas_juego.bind("<Up>", rotar)
    canvas_juego.bind("<Down>", abajo)
    
    bucle_del_juego()
    

    
principal.mainloop()