import tkinter as tk
from configuracion import *
from login.login import *       # Importa la función ingreso desde login.py en la carpeta login
from screens.main import *

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Let's Move app")
ventana.geometry("292x543")

def main():
    frame1 = tk.Frame(ventana, bg="blue", width=292, height=(543 * 0.5))
    frame1.pack(side=tk.TOP, fill="both", expand=True)

    label1 = tk.Label(frame1, text="Bienvenido a Let's Move!", font=("Arial", 12), bg="blue", fg="white")
    label1.pack(side=tk.TOP, fill="both", expand=True)

    frame2 = tk.Frame(ventana, bg="black", width=292, height=(543 * 0.5))
    frame2.pack(side=tk.BOTTOM, fill="both", expand=False)

    tk.Button(frame2, text="Iniciar Sesión", font=("Arial", 12), bg="yellow", fg="white", command=lambda: ingreso(ventana, main)).pack(side=tk.LEFT, fill="both", expand=False)
    tk.Button(frame2, text="Registrarse", font=("Arial", 12), bg="yellow", fg="white", command=lambda: registro(ventana, main)).pack(side=tk.RIGHT, fill="both", expand=False)

main()
ventana.mainloop()