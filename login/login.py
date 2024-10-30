import tkinter as tk
import sys
import os

# Agrega la ruta del directorio padre al sistema para permitir la importación de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from configuracion.configr import *  # Importa configuraciones específicas
from screens.main import *  # Importa funciones desde el módulo principal

def registro_paso2(ventana, main):
    """Muestra el segundo paso del registro con campos adicionales."""
    # Limpia todos los widgets de la ventana
    for widget in ventana.winfo_children():
        widget.destroy()
    
    # Crea un marco para el segundo paso del registro
    frame2 = tk.Frame(ventana, bg="black", width=292, height=(543 * 0.4))
    frame2.pack(side=tk.BOTTOM, fill="both", expand=True)

    # Define las etiquetas y los nombres de los campos
    labels = ["Nombre de usuario:", "Nombre:", "Apellido:"]
    entry_names = ["username", "nombre", "apellido"]

    # Crea etiquetas y campos de entrada para cada elemento
    for label_text, entry_name in zip(labels, entry_names):
        label = tk.Label(frame2, text=label_text, font=("Arial", 12), bg="black", fg="white")
        label.pack(side=tk.TOP, fill="both", expand=True)

        entry = tk.Entry(frame2, width=292, fg="grey")  # Campo de entrada
        entry.pack(side=tk.TOP, fill="both", expand=True)
        # Asigna funciones para limpiar y establecer el placeholder
        entry.bind("<FocusIn>", lambda e, entry=entry, placeholder=placeholders[entry_name]: clear_placeholder(entry, placeholder))
        entry.bind("<FocusOut>", lambda e, entry=entry, placeholder=placeholders[entry_name]: set_placeholder(entry, placeholder))
        set_placeholder(entry, placeholders[entry_name])  # Establece el placeholder al inicio

    # Crea un marco para los botones
    frame_boton = tk.Frame(frame2, bg="black")
    frame_boton.pack(side=tk.BOTTOM, fill="both", expand=True)

    # Botón para registrar
    tk.Button(frame_boton, text="Registrar", font=("Arial", 12), bg="black", fg="white", command=lambda: main_screen(ventana)).pack(side=tk.LEFT, fill="both", expand=True)
    # Botón para volver al paso anterior
    tk.Button(frame_boton, text="Volver", font=("Arial", 12), bg="black", fg="white", command=lambda: volver(ventana, main)).pack(side=tk.RIGHT, fill="both", expand=True)

def registro(ventana, main):
    """Muestra la primera parte del registro con email y contraseña."""
    # Limpia todos los widgets de la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

    # Crea un marco para la primera parte del registro
    frame2 = tk.Frame(ventana, bg="black", width=292, height=(543 * 0.4))
    frame2.pack(side=tk.BOTTOM, fill="both", expand=True)

    # Etiqueta y campo de entrada para el email
    label2 = tk.Label(frame2, text="Email:", font=("Arial", 12), bg="black", fg="white")
    label2.pack(side=tk.TOP, fill="both", expand=True)

    email = tk.Entry(frame2, width=292, fg="grey")
    email.pack(side=tk.TOP, fill="both", expand=True)
    # Asigna funciones para limpiar y establecer el placeholder
    email.bind("<FocusIn>", lambda e: clear_placeholder(email, placeholders["email"]))
    email.bind("<FocusOut>", lambda e: set_placeholder(email, placeholders["email"]))
    set_placeholder(email, placeholders["email"])

    # Etiqueta y campo de entrada para la contraseña
    label3 = tk.Label(frame2, text="Password:", font=("Arial", 12), bg="black", fg="white")
    label3.pack(side=tk.TOP, fill="both", expand=True)

    password = tk.Entry(frame2, width=292, show='*', fg="grey")  # Campo de entrada para contraseña
    password.pack(side=tk.TOP, fill="both", expand=True)
    # Asigna funciones para limpiar y establecer el placeholder
    password.bind("<FocusIn>", lambda e: clear_placeholder(password, placeholders["password"]))
    password.bind("<FocusOut>", lambda e: set_placeholder(password, placeholders["password"]))
    set_placeholder(password, placeholders["password"])

    # Crea un marco para los botones
    frame_boton = tk.Frame(frame2, bg="black")
    frame_boton.pack(side=tk.BOTTOM, fill="both", expand=True)

    # Botón para avanzar al siguiente paso
    tk.Button(frame_boton, text="Siguiente", font=("Arial", 12), bg="black", fg="white", command=lambda: registro_paso2(ventana, main)).pack(side=tk.RIGHT, fill="both", expand=True)
    # Botón para volver
    tk.Button(frame_boton, text="Volver", font=("Arial", 12), bg="black", fg="white", command=lambda: volver(ventana, main)).pack(side=tk.LEFT, fill="both", expand=True)

def ingreso(ventana, main):
    """Muestra la interfaz de ingreso de email y contraseña."""
    # Limpia todos los widgets de la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

    # Crea un marco para la interfaz de ingreso
    frame2 = tk.Frame(ventana, bg="black", width=292, height=(543 * 0.4))
    frame2.pack(side=tk.BOTTOM, fill="both", expand=True)

    # Etiqueta y campo de entrada para el email
    tk.Label(frame2, text="Email:", font=("Arial", 12), bg="black", fg="white").pack(side=tk.TOP, fill="both", expand=True)
    email = tk.Entry(frame2, width=292, fg="grey")
    email.pack(side=tk.TOP, fill="both", expand=True)
    # Asigna funciones para limpiar y establecer el placeholder
    email.bind("<FocusIn>", lambda e: clear_placeholder(email, placeholders["email"]))
    email.bind("<FocusOut>", lambda e: set_placeholder(email, placeholders["email"]))
    set_placeholder(email, placeholders["email"])

    # Etiqueta y campo de entrada para la contraseña
    tk.Label(frame2, text="Password:", font=("Arial", 12), bg="black", fg="white").pack(side=tk.TOP, fill="both", expand=True)
    password = tk.Entry(frame2, width=292, show='*', fg="grey")
    password.pack(side=tk.TOP, fill="both", expand=True)
    # Asigna funciones para limpiar y establecer el placeholder
    password.bind("<FocusIn>", lambda e: clear_placeholder(password, placeholders["password"]))
    password.bind("<FocusOut>", lambda e: set_placeholder(password, placeholders["password"]))
    set_placeholder(password, placeholders["password"])

    # Crea un marco para los botones
    frame_boton = tk.Frame(frame2, bg="black")
    frame_boton.pack(side=tk.BOTTOM, fill="both", expand=True)

    # Botón para ingresar
    tk.Button(frame_boton, text="Ingresar", font=("Arial", 12), bg="black", fg="white", command=lambda: main_screen(ventana, logged_in=True)).pack(side=tk.RIGHT, fill="both", expand=True)
    # Botón para volver
    tk.Button(frame_boton, text="Volver", font=("Arial", 12), bg="black", fg="white", command=lambda: volver(ventana, main)).pack(side=tk.LEFT, fill="both", expand=True)
