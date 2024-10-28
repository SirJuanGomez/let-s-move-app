import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from configuracion.api import *
from tkinter import Canvas
from datetime import datetime, timedelta



# Inicialización de valores actuales y fijos
current_values = {
    "steps": 0,
    "calories": 0,
    "distance": 0
}

fixed_values = {
    "steps": 10000,
    "calories": 2000,
    "distance": 5.0
}


def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def deslizador(master):
    def update_label(value):
        options = ["Hoy", "Semana", "Mes"]
        label.config(text=f"Seleccionado: {options[int(value)]}")

    # Crear un deslizador con 3 opciones
    slider = tk.Scale(
        master,
        from_=0,
        to=2,
        orient='horizontal',
        command=update_label,
        length=300,
        sliderlength=20,
        bg="#e0e0e0",
        fg="#007acc",
        highlightbackground="#f0f0f0",
        troughcolor="#c0c0c0"
    )
    slider.pack(pady=10)

    # Crear una etiqueta para mostrar la opción seleccionada
    label = tk.Label(master, text="Seleccionado: Hoy", font=("Arial", 12), bg="#f0f0f0")
    label.pack(pady=5)

    # Crear etiquetas para las opciones
    options_frame = tk.Frame(master, bg="#f0f0f0")
    options_frame.pack()

    options = ["Hoy", "Semana", "Mes"]
    for i, option in enumerate(options):
        option_label = tk.Label(
            options_frame,
            text=option,
            font=("Arial", 10),
            bg="#f0f0f0",
            width=10,
            anchor="center"
        )
        option_label.grid(row=0, column=i, padx=(0, 10) if i < len(options) - 1 else 0)


def mostrar_grafico_barras(graph_frame, calorias_semanales, calorias_mensuales):
    altura_maxima = 200  # Altura máxima para el gráfico
    meta_semanal = 10000  # Ajusta según tu meta
    meta_mensual = 40000  # Ajusta según tu meta

    # Calcular proporción para las barras
    proporcion_semanal = min(calorias_semanales / meta_semanal, 1) * altura_maxima if calorias_semanales is not None else 0
    proporcion_mensual = min(calorias_mensuales / meta_mensual, 1) * altura_maxima if calorias_mensuales is not None else 0

    # Limpiar el marco gráfico antes de dibujar
    for widget in graph_frame.winfo_children():
        widget.destroy()

    # Crear las barras
    barra_semanal = tk.Canvas(graph_frame, width=50, height=altura_maxima)
    barra_semanal.create_rectangle(0, altura_maxima - proporcion_semanal, 50, altura_maxima, fill="blue")
    barra_semanal.pack(side=tk.LEFT)
    
    # Etiqueta para las calorías semanales
    etiqueta_semanal = tk.Label(graph_frame, text=f'Semanal: {calorias_semanales}')
    etiqueta_semanal.pack(side=tk.LEFT)

    barra_mensual = tk.Canvas(graph_frame, width=50, height=altura_maxima)
    barra_mensual.create_rectangle(0, altura_maxima - proporcion_mensual, 50, altura_maxima, fill="green")
    barra_mensual.pack(side=tk.LEFT)

    # Etiqueta para las calorías mensuales
    etiqueta_mensual = tk.Label(graph_frame, text=f'Mensual: {calorias_mensuales}')
    etiqueta_mensual.pack(side=tk.LEFT)

    # Leyenda
    leyenda_frame = tk.Frame(graph_frame)
    leyenda_frame.pack(side=tk.LEFT)
    tk.Label(leyenda_frame, text="Leyenda:").pack()
    tk.Label(leyenda_frame, text="Azul: Calorías Semanales").pack()
    tk.Label(leyenda_frame, text="Verde: Calorías Mensuales").pack()

def update_pie_charts():
    global current_values

    current_values["steps"] = get_steps() or 0
    current_values["calories"] = get_calories() or 0
    current_values["distance"] = get_distance() * 1000 or 0

    for pie_chart in pie_charts:
        pie_chart.update(current_values[pie_chart.data_type], fixed_values[pie_chart.data_type])

# Lista para almacenar los gráficos de pastel
pie_charts = []

# Clase para crear un gráfico de pastel
class PieChart:
    def __init__(self, canvas, center_x, center_y, radius, color, data_type):
        self.canvas = canvas
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color
        self.data_type = data_type

    def draw_empty(self):
        # Dibuja un círculo vacío
        self.canvas.create_oval(
            self.center_x - self.radius, self.center_y - self.radius,
            self.center_x + self.radius, self.center_y + self.radius,
            outline='gray', width=2
        )

    def clear_canvas(self):
        self.canvas.delete("all")

    def draw(self, angle):
        self.clear_canvas()
        self.canvas.create_arc(
            self.center_x - self.radius, self.center_y - self.radius,
            self.center_x + self.radius, self.center_y + self.radius,
            start=0, extent=angle,  # Gráfica de pastel
            fill=self.color, outline=self.color
        )

    def update(self, value, fixed_value):
        percentage = (value / fixed_value) * 360  # Convertir a grados
        self.draw(percentage)


