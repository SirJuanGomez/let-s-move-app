import tkinter as tk
from PIL import Image, ImageTk
from configuracion.configr import *
from configuracion.utils import *
from screens.calorias import *
from screens.pasos import *
from screens.distancia import *
from screens.mas_opciones import *

tamaño_botones = (284, 60)

def main_screen(ventana, logged_in=True):
    limpiar_ventana(ventana)

    # Mantener las imágenes como atributos del objeto ventana para que no se liberen
    ventana.img_calorias = cargar_imagen("img/icon_calorias.png", tamaño_botones)
    ventana.img_distancia = cargar_imagen("img/icon_distancia.png", tamaño_botones)
    ventana.img_pasos = cargar_imagen("img/icon_pasos.png", tamaño_botones)
    ventana.img_mas = cargar_imagen("img/icon_mas.png", tamaño_botones)
    ventana.img_cerrar = cargar_imagen("img/icon_cerrar.png", tamaño_botones)  # Cargar imagen de cerrar
    
    # Crear frame principal
    main_frame = tk.Frame(ventana, bg="white")
    main_frame.pack(expand=True, fill=tk.BOTH)

    # Label de inicio
    label_start = tk.Label(main_frame, text="INICIO", bg="white", font=("Intensa Fuente", 70), height=2)
    label_start.pack()

    # Configuración de los botones con las imágenes
    botones_config = [
        ("Calorías", ventana.img_calorias, interfaz_calorias),
        ("Pasos", ventana.img_pasos, interfaz_pasos),
        ("Distancia", ventana.img_distancia, interfaz_distancia),
        ("Más Opciones", ventana.img_mas, interfaz_mas_opciones)
    ]

    for texto, imagen, comando in botones_config:
        frame = tk.Frame(main_frame, width=284, height=60, bg="white")
        frame.pack_propagate(False)
        frame.pack(pady=(10, 0))

        boton = tk.Button(frame, image=imagen, command=lambda cmd=comando: cmd(ventana))
        boton.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Botón de "Volver" si no ha iniciado sesión
    if not logged_in:
        tk.Button(main_frame, text="Volver a Registrar", command=lambda: volver(ventana, None)).pack(pady=(10, 0))

    # Crear frame y botón "Cerrar" con la misma apariencia y una imagen
    frame_cerrar = tk.Frame(main_frame, width=284, height=60, bg="white")
    frame_cerrar.pack_propagate(False)
    frame_cerrar.pack(pady=(160, 0))

    boton_cerrar = tk.Button(frame_cerrar, image=ventana.img_cerrar, command=ventana.destroy)
    boton_cerrar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
