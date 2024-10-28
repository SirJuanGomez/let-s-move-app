import tkinter as tk
from configuracion.configr import *

def main_screen(ventana, logged_in=True):
    limpiar_ventana(ventana)
    # Crear frame principal
    main_frame = tk.Frame(ventana, bg="white")
    main_frame.pack(expand=True, fill=tk.BOTH)

    # Label de inicio que ocupa las dos columnas en la fila 0
    label_start = tk.Label(main_frame, text="INICIO", bg="white", font=("Intensa Fuente", 70))
    label_start.pack()

    


    # Agregar botón de "Volver" solo si el usuario no ha iniciado sesión
    if not logged_in:
        tk.Button(main_frame, text="Volver a Registrar", command=lambda: volver(ventana, None)).grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Asegúrate de que las funciones como interfaz_calorias, etc. estén definidas y sean accesibles.
