import tkinter as tk

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def interfaz_mas_opciones(master):
    frame_mas = tk.Frame(master, bg="white")
    frame_mas.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(frame_mas, text="Interfaz de Más Funciones", bg="white")
    label.pack(pady=20)

    boton_volver = tk.Button(frame_mas, text="Volver", command=lambda: limpiar_ventana(master))
    boton_volver.pack(pady=10)
