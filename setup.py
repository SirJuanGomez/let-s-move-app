import os
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

# Lista de librerías a instalar
librerias = [
    "matplotlib",
    "pillow",
    "requests",
    "fpdf"
]

def instalar_librerias():
    for libreria in librerias:
        # Actualiza la barra de progreso
        progress['value'] += 100 / len(librerias)
        ventana.update_idletasks()  # Actualiza la interfaz
        # Instala la librería
        subprocess.call(['pip', 'install', libreria])
    
    # Mensaje de finalización
    messagebox.showinfo("Instalación completa", "Todas las librerías han sido instaladas, Ejecuta app.py.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Instalación de librerías")
ventana.geometry("300x150")

# Crear barra de progreso
progress = ttk.Progressbar(ventana, orient="horizontal", length=250, mode="determinate")
progress.pack(pady=20)

# Botón para iniciar la instalación
boton_instalar = tk.Button(ventana, text="Instalar librerías", command=instalar_librerias)
boton_instalar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
