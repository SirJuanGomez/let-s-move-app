import tkinter as tk

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def interfaz_distancia(master):
    frame_distancia = tk.Frame(master, bg="white")
    frame_distancia.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(frame_distancia, text="Interfaz de Distancia", bg="white")
    label.pack(pady=20)

    boton_volver = tk.Button(frame_distancia, text="Volver", command=lambda: limpiar_ventana(master))
    boton_volver.pack(pady=10)
