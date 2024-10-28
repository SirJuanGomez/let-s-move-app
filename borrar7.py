import tkinter as tk
from configuracion.configr import *

def main_screen(ventana, logged_in=True):
    """Muestra la pantalla principal después de iniciar sesión."""
    for widget in ventana.winfo_children():
        widget.destroy()
    
    # Crear frame principal
    main_frame = tk.Frame(ventana, bg="white")
    main_frame.pack()

    # Label de inicio que ocupa las dos columnas en la fila 0
    label_start = tk.Label(main_frame, text="INICIO", bg="white", font=("Intensa Fuente", 70))
    label_start.grid(row=0, column=0, columnspan=2, pady=(10, 0))  # Ocupa 2 columnas

    # Crear botones en la matriz 2x2 en la fila 1 y 2
    frame_calorias = tk.Frame(main_frame, bg="white", width=160, height=160)
    frame_calorias.grid(row=1, column=0, padx=10, pady=10)
    crear_boton(frame_calorias, "calorias", (100, 100))

    frame_distancia = tk.Frame(main_frame, bg="white", width=160, height=160)
    frame_distancia.grid(row=1, column=1, padx=10, pady=10)
    crear_boton(frame_distancia, "distancia", (100, 100))

    frame_pasos = tk.Frame(main_frame, bg="white", width=160, height=160)
    frame_pasos.grid(row=2, column=0, padx=10, pady=10)
    crear_boton(frame_pasos, "pasos", (100, 100))

    frame_registros = tk.Frame(main_frame, bg="white", width=160, height=160)
    frame_registros.grid(row=2, column=1, padx=10, pady=10)
    crear_boton(frame_registros, "registros", (100, 100))

    # Botón de más opciones que ocupa las dos columnas en la fila 3
    frame_more = tk.Frame(main_frame, bg="white", width=367, height=40)
    frame_more.grid(row=3, column=0, columnspan=2, pady=(10, 10))  # Ocupa 2 columnas
    crear_boton(frame_more, "mas", (100, 100))

    # Agregar botón de "Volver" solo si el usuario no ha iniciado sesión
    if not logged_in:
        tk.Button(main_frame, text="Volver a Registrar", command=lambda: volver(ventana, None)).grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Asegúrate de que las funciones como interfaz_calorias, etc. estén definidas y sean accesibles.