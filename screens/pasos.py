import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
from configuracion.utils import *
from configuracion.configr import *
from configuracion.api import *

def interfaz_pasos(ventana):
    # Importa la pantalla principal para permitir la navegación de vuelta
    from screens.main import main_screen
    # Limpia la ventana actual de cualquier widget
    limpiar_ventana(ventana)
    img_Back = Image.open("img/img_Back.png").resize((150, 50), Image.LANCZOS)
    img_Back = ImageTk.PhotoImage(img_Back)

    # Crea el marco principal de la interfaz con un fondo azul
    frame_main = tk.Frame(ventana, bg="white")
    frame_main.pack(fill=tk.BOTH, expand=True)

    # Crea un marco para los gráficos con un fondo rojo
    frame_graphica = tk.Frame(frame_main, bg="white", height=543, width=292)
    frame_graphica.pack(fill=tk.BOTH, expand=True)

    # Crea el gráfico de pasos por defecto para "Hoy"
    crear_graficos_pasos(frame_graphica, "Hoy")

    # Variable para almacenar el tipo de gráfico seleccionado
    graph_type_var = tk.StringVar(value="Hoy")
    graph_options = ["Hoy", "Semana", "Mes"]  # Opciones de gráfico

    # Etiqueta para el selector de tipo de gráfico
    label_selector = tk.Label(frame_main, text="Selecione el tipo de Grafica::", bg="white", fg="black", font=("Arial", 12))
    label_selector.pack(pady=5)

    # Crea un menú desplegable para seleccionar el tipo de gráfico
    option_menu = ttk.OptionMenu(
        frame_main,
        graph_type_var,
        graph_options[0],
        *graph_options,
        command=lambda _: crear_graficos_pasos(frame_graphica, graph_type_var.get())
    )
    option_menu.pack(pady=5)  # Espaciado vertical

    # Botón para regresar a la pantalla principal
    back_button = tk.Button(
        frame_main,
        text="Volver",
        command=lambda: main_screen(ventana),  # Regresa a la pantalla principal
        bg="white",
        fg="black",
        font=("Arial", 12)
    )
    back_button.pack(pady=10)  # Espaciado vertical
