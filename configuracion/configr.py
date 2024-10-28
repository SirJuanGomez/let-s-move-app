
# Importaciones de librerías
import tkinter as tk
from configuracion.api import *
from configuracion.utils import limpiar_ventana
from PIL import Image, ImageTk
from screens.calorias import interfaz_calorias
from screens.distancia import interfaz_distancia
from screens.pasos import interfaz_pasos
from screens.registros import interfaz_registros
from screens.mas_opciones import interfaz_mas_opciones

placeholders = {
    "email": "Ingresa tu email",
    "password": "Ingresa tu contraseña",
    "username": "Ingresa tu nombre de usuario",
    "nombre": "Ingresa tu nombre",
    "apellido": "Ingresa tu apellido"
}

# Función para crear un frame
def crear_frame(conten_frame, bg_color, width, height, x, y):
    frame = tk.Frame(conten_frame, bg=bg_color, width=width, height=height)
    frame.place(x=x, y=y)
    return frame

# Funciones para cargar imágenes
def cargar_imagen(ruta, tamaño):
    try:
        img = Image.open(ruta)
        img = img.resize(tamaño, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        return None
    
def aplicar_alpha(color, alpha):
    r, g, b = color
    r = int((1 - alpha) * 255 + alpha * r)
    g = int((1 - alpha) * 255 + alpha * g)
    b = int((1 - alpha) * 255 + alpha * b)
    
    return f'#{r:02x}{g:02x}{b:02x}'

# Función para crear botones
def crear_boton(frame, tipo, tamaño=(100, 100)):
    """Crea un botón con una imagen y texto en el frame dado."""
    imagenes = {
        "calorias": ('img/icon_calories.png', "Calorías"),
        "distancia": ('img/test.png', "Distancia"),  # Cambiado a test.png
        "pasos": ('img/test.png', "Pasos"),           # Cambiado a test.png
        "registros": ('img/test.png', "Registros"),   # Cambiado a test.png
        "mas": ('img/test.png', "Más"),               # Cambiado a test.png
        "volver": ('img/test.png', "Volver"),         # Cambiado a test.png
    }

    if tipo not in imagenes:
        print(f"No hay configuración para el tipo: {tipo}")
        return

    imagen_ruta, texto = imagenes[tipo]
    img = cargar_imagen(imagen_ruta, tamaño)
    if img is None:
        return

    # Estilo del botón
    fondo_color = (76, 175, 80)
    fondo_hover = (69, 160, 73)

    ancho = img.width()
    alto = img.height()
    boton_canvas = tk.Canvas(frame, width=ancho, height=alto, bg="red", highlightthickness=0)

    # Función para dibujar el botón
    def dibujar_boton(color, alpha=0):
        boton_canvas.delete("all")
        bg_color = aplicar_alpha(color, alpha)
        boton_canvas.create_rectangle(0, 0, ancho, alto, fill=bg_color, outline="")
        boton_canvas.config(bg=bg_color)
        boton_canvas.create_image(ancho // 2, alto // 2, image=img)
        boton_canvas.create_text(ancho // 2, alto // 2, text=texto, font=("Intensa Fuente", 12), fill="White", anchor="center")

    dibujar_boton(fondo_color)

    def abrir_interfaz():
        limpiar_ventana(frame)
        if tipo == "calorias":
            interfaz_calorias(frame.master)
        elif tipo == "distancia":
            interfaz_distancia(frame.master)
        elif tipo == "pasos":
            interfaz_pasos(frame.master)
        elif tipo == "registros":
            interfaz_registros(frame.master)
        elif tipo == "mas":
            interfaz_mas_opciones(frame.master)
        elif tipo == "volver":
            limpiar_ventana(frame.master)
            pass
        else:
            print(f"error: no se reconoce el tipo de botón: {tipo}")

    # Eventos del botón
    boton_canvas.bind("<Button-1>", lambda event: abrir_interfaz())
    boton_canvas.bind("<Enter>", lambda event: dibujar_boton(fondo_hover, alpha=0.2))
    boton_canvas.bind("<Leave>", lambda event: dibujar_boton(fondo_color, alpha=0))

    boton_canvas.pack(pady=10)
    
def set_placeholder(entry, placeholder):
    """Establece un placeholder en el campo de entrada."""
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="grey")  # Cambia el color del texto a gris

def clear_placeholder(entry, placeholder):
    """Limpia el placeholder cuando el campo recibe el foco."""
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black")  # Cambia el color del texto a negro

def volver(ventana, main):
    """Limpia la ventana y vuelve a la pantalla principal."""
    for widget in ventana.winfo_children():
        widget.destroy()
    main()