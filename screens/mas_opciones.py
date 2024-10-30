import tkinter as tk
from fpdf import FPDF
from configuracion.utils import *
from configuracion.configr import *
from PIL import Image, ImageTk  # Importa Image y ImageTk para trabajar con imágenes
import os

def interfaz_mas_opciones(ventana):
    # Importa la pantalla principal
    from screens.main import main_screen
    limpiar_ventana(ventana)  # Limpia la ventana actual

    # Carga y redimensiona las imágenes para los botones
    img_PDF = Image.open("img/img_PDF.png").resize((150, 50), Image.LANCZOS)
    img_PDF = ImageTk.PhotoImage(img_PDF)
    img_Back = Image.open("img/img_Back.png").resize((150, 50), Image.LANCZOS)
    img_Back = ImageTk.PhotoImage(img_Back)

    # Crea un marco principal con fondo azul
    frame_main = tk.Frame(ventana, bg="white")
    frame_main.pack(fill=tk.BOTH, expand=True)

    # Marco para los botones
    frame_boton = tk.Frame(frame_main, bg="white")
    frame_boton.pack(pady=20)

    # Mantiene referencias a las imágenes para evitar que sean recolectadas por el recolector de basura
    frame_main.img_PDF = img_PDF
    frame_main.img_Back = img_Back

    # Botón para generar el PDF
    boton_pdf = tk.Button(
        frame_boton,
        text="Generar PDF",
        image=img_PDF,
        command=lambda: crear_pdf_con_graficos(frame_main),  # Llama a la función para crear PDF al hacer clic
        bg="white",
        fg="black",
        font=("Arial", 12)
    )
    boton_pdf.pack(side=tk.TOP, pady=50)

    # Botón para volver a la pantalla principal
    boton_volver = tk.Button(
        frame_boton,
        text="Volver",
        image=img_Back,
        command=lambda: main_screen(ventana),  # Vuelve a la pantalla principal
        bg="white",
        fg="black",
        font=("Arial", 12)
    )
    boton_volver.pack(side=tk.TOP, pady=50)

    # Función para crear el PDF con gráficos
    def crear_pdf_con_graficos(frame):
        grafica_paths = []  # Lista para almacenar las rutas de los gráficos
        
        # Genera gráficos para "Hoy", "Semana" y "Mes"
        for graph_type in ["Hoy", "Semana", "Mes"]:
            grafica_path = crear_graficos_combinados(graph_type)  # Crea los gráficos combinados
            grafica_paths.append(grafica_path)  # Agrega la ruta del gráfico a la lista

        # Define la ruta del PDF donde se guardará
        pdf_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report', 'graficos_combinados.pdf')
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)  # Crea el directorio si no existe

        pdf = FPDF()  # Crea una instancia de FPDF
        
        try:
            # Agrega cada gráfico al PDF
            for grafica_path in grafica_paths:
                pdf.add_page()  # Agrega una nueva página al PDF
                with Image.open(grafica_path) as img:  # Abre el gráfico
                    width, height = img.size  # Obtiene las dimensiones del gráfico
                    width_mm = width * 0.264583  # Convierte píxeles a milímetros
                    height_mm = height * 0.264583
                    margin = 20  # Define un margen
                    # Añade la imagen al PDF
                    pdf.image(grafica_path, x=margin, y=margin, w=pdf.w - 2 * margin, h=height_mm)

            # Guarda el PDF en la ruta definida
            pdf.output(pdf_path)
            print("PDF guardado correctamente.")
        except Exception as e:
            # Manejo de errores al guardar el PDF
            print(f"Error al guardar el PDF: {e}")

        # Muestra un mensaje indicando que el PDF fue guardado
        label_exito = tk.Label(frame, text=f'PDF guardado como "{pdf_path}"', font=('Arial', 12))
        label_exito.grid(row=1, column=0, padx=5, pady=5)
