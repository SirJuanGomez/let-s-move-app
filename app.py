import tkinter as tk
from configuracion import *  # Importa configuraciones necesarias
from login.login import *  # Importa la función ingreso desde login.py en la carpeta login
from screens.main import *  # Importa funciones o clases desde el módulo principal
from PIL import Image, ImageTk  # Importa Image y ImageTk para trabajar con imágenes

# Crear la ventana principal
ventana = tk.Tk()  # Inicializa la ventana principal de la aplicación
ventana.title("Let's Move app")  # Establece el título de la ventana
ventana.geometry("375x812")  # Establece las dimensiones de la ventana

def main():
    # Cargar y redimensionar la imagen para el botón de ingreso
    img_ingreso = Image.open("img/img_inicio.png").resize((150, 50), Image.LANCZOS)
    img_ingreso = ImageTk.PhotoImage(img_ingreso)  # Convierte la imagen a un formato que Tkinter puede usar
    ventana.img_ingreso = img_ingreso  # Mantiene una referencia a la imagen para evitar que se recoja como basura

    # Cargar y redimensionar la imagen para el botón de registro
    img_registro = Image.open("img/img_registro.png").resize((150, 50), Image.LANCZOS)
    img_registro = ImageTk.PhotoImage(img_registro)  # Convierte la imagen a un formato que Tkinter puede usar
    ventana.img_registro = img_registro  # Mantiene una referencia a la imagen

    # Crear un marco en la parte superior para el mensaje de bienvenida
    frame1 = tk.Frame(ventana, bg="white", width=292, height=(543 * 0.5))
    frame1.pack(side=tk.TOP, fill="both", expand=True)  # Agrega el marco a la ventana

    # Etiqueta de bienvenida
    label1 = tk.Label(frame1, text="Bienvenido a Let's Move!", font=("Arial", 20), bg="white", fg="black")
    label1.pack(side=tk.TOP, fill="both", expand=True)  # Agrega la etiqueta al marco

    # Crear un marco en la parte inferior para los botones de acción
    frame2 = tk.Frame(ventana, bg="white", width=292, height=(543 * 0.5))
    frame2.pack(side=tk.BOTTOM, fill="both", expand=False)  # Agrega el marco a la ventana

    # Botón para iniciar sesión
    tk.Button(frame2, text="Iniciar Sesión", image=img_ingreso, font=("Arial", 12), bg="black", fg="white",
              command=lambda: ingreso(ventana, main)).pack(side=tk.LEFT, fill="both", expand=False, padx=10, pady=10)
    
    # Botón para registrarse
    tk.Button(frame2, text="Registrarse", image=img_registro, font=("Arial", 12), bg="black", fg="white",
              command=lambda: registro(ventana, main)).pack(side=tk.RIGHT, fill="both", expand=False, padx=10, pady=10)

# Llama a la función main para inicializar la interfaz
main()
ventana.mainloop()  # Inicia el bucle principal de la interfaz gráfica
