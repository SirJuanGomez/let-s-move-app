import tkinter as tk

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def interfaz_pasos(master):
    frame_pasos = tk.Frame(master, bg="white")
    frame_pasos.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(frame_pasos, text="Interfaz de Pasos", bg="white")
    label.pack(pady=20)

    boton_volver = tk.Button(frame_pasos, text="Volver", command=lambda: limpiar_ventana(master))
    boton_volver.pack(pady=10)
