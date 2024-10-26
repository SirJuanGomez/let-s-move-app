# login.py
import tkinter as tk
from config.config import set_placeholder, clear_placeholder, placeholders

def volver(ventana, main):
    """Limpia la ventana y vuelve a la pantalla principal."""
    for widget in ventana.winfo_children():
        widget.destroy()
    main()

def registro_paso2(ventana, main):
    """Muestra el segundo paso del registro con campos adicionales."""
    for widget in ventana.winfo_children():
        widget.destroy()
    
    frame2 = tk.Frame(ventana, bg="black", width=292, height=(543 * 0.4))
    frame2.pack(side=tk.BOTTOM, fill="both", expand=True)

    labels = ["Nombre de usuario:", "Nombre:", "Apellido:"]
    entry_names = ["username", "nombre", "apellido"]

    for label_text, entry_name in zip(labels, entry_names):
        label = tk.Label(frame2, text=label_text, font=("Arial", 12), bg="black", fg="white")
        label.pack(side=tk.TOP, fill="both", expand=True)

        entry = tk.Entry(frame2, width=292, fg="grey")
        entry.pack(side=tk.TOP, fill="both", expand=True)
        entry.bind("<FocusIn>", lambda e, entry=entry, placeholder=placeholders[entry_name]: clear_placeholder(entry, placeholder))
        entry.bind("<FocusOut>", lambda e, entry=entry, placeholder=placeholders[entry_name]: set_placeholder(entry, placeholder))
        set_placeholder(entry, placeholders[entry_name])

    frame_boton = tk.Frame(frame2, bg="black")
    frame_boton.pack(side=tk.BOTTOM, fill="both", expand=True)

    tk.Button(frame_boton, text="Registrar", font=("Arial", 12), bg="black", fg="white").pack(side=tk.LEFT, fill="both", expand=True)
    tk.Button(frame_boton, text="Volver", font=("Arial", 12), bg="black", fg="white", command=lambda: volver(ventana, main)).pack(side=tk.RIGHT, fill="both", expand=True)

def registro(ventana, main):
    """Muestra la primera parte del registro con email y contraseña."""
    for widget in ventana.winfo_children():
        widget.destroy()

    frame2 = tk.Frame(ventana, bg="black", width=292, height=(543 * 0.4))
    frame2.pack(side=tk.BOTTOM, fill="both", expand=True)

    label2 = tk.Label(frame2, text="Email:", font=("Arial", 12), bg="black", fg="white")
    label2.pack(side=tk.TOP, fill="both", expand=True)

    email = tk.Entry(frame2, width=292, fg="grey")
    email.pack(side=tk.TOP, fill="both", expand=True)
    email.bind("<FocusIn>", lambda e: clear_placeholder(email, placeholders["email"]))
    email.bind("<FocusOut>", lambda e: set_placeholder(email, placeholders["email"]))
    set_placeholder(email, placeholders["email"])

    label3 = tk.Label(frame2, text="Password:", font=("Arial", 12), bg="black", fg="white")
    label3.pack(side=tk.TOP, fill="both", expand=True)

    password = tk.Entry(frame2, width=292, show='*', fg="grey")
    password.pack(side=tk.TOP, fill="both", expand=True)
    password.bind("<FocusIn>", lambda e: clear_placeholder(password, placeholders["password"]))
    password.bind("<FocusOut>", lambda e: set_placeholder(password, placeholders["password"]))
    set_placeholder(password, placeholders["password"])

    frame_boton = tk.Frame(frame2, bg="black")
    frame_boton.pack(side=tk.BOTTOM, fill="both", expand=True)

    tk.Button(frame_boton, text="Siguiente", font=("Arial", 12), bg="black", fg="white", command=lambda: registro_paso2(ventana, main)).pack(side=tk.RIGHT, fill="both", expand=True)
    tk.Button(frame_boton, text="Volver", font=("Arial", 12), bg="black", fg="white", command=lambda: volver(ventana, main)).pack(side=tk.LEFT, fill="both", expand=True)

def ingreso(ventana, main):
    """Muestra la interfaz de ingreso de email y contraseña."""
    for widget in ventana.winfo_children():
        widget.destroy()

    frame2 = tk.Frame(ventana, bg="black", width=292, height=(543 * 0.4))
    frame2.pack(side=tk.BOTTOM, fill="both", expand=True)

    tk.Label(frame2, text="Email:", font=("Arial", 12), bg="black", fg="white").pack(side=tk.TOP, fill="both", expand=True)
    email = tk.Entry(frame2, width=292, fg="grey")
    email.pack(side=tk.TOP, fill="both", expand=True)
    set_placeholder(email, placeholders["email"])

    tk.Label(frame2, text="Password:", font=("Arial", 12), bg="black", fg="white").pack(side=tk.TOP, fill="both", expand=True)
    password = tk.Entry(frame2, width=292, show='*', fg="grey")
    password.pack(side=tk.TOP, fill="both", expand=True)
    set_placeholder(password, placeholders["password"])

    frame_boton = tk.Frame(frame2, bg="black")
    frame_boton.pack(side=tk.BOTTOM, fill="both", expand=True)

    tk.Button(frame_boton, text="Ingresar", font=("Arial", 12), bg="black", fg="white").pack(side=tk.RIGHT, fill="both", expand=True)
    tk.Button(frame_boton, text="Volver", font=("Arial", 12), bg="black", fg="white", command=lambda: volver(ventana, main)).pack(side=tk.LEFT, fill="both", expand=True)
