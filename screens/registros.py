import tkinter as tk

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def interfaz_registros(master):
    frame_registros = tk.Frame(master, bg="white")
    frame_registros.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(frame_registros, text="Interfaz de Registros", bg="white")
    label.pack(pady=20)

    boton_volver = tk.Button(frame_registros, text="Volver", command=lambda: limpiar_ventana(master))
    boton_volver.pack(pady=10)
