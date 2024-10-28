import tkinter as tk
import matplotlib.pyplot as plt
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
from configuracion.api import *

def interfaz_calorias(ventana):
    
    frame = tk.Frame(ventana)
    frame.pack(fill=tk.BOTH, expand=True)

    # Crear un widget de texto con un scrollbar
    text_area = tk.Text(frame, wrap='word')
    scrollbar = tk.Scrollbar(frame, command=text_area.yview)
    text_area.config(yscrollcommand=scrollbar.set)

    # Empaquetar los widgets
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Agregar algo de texto para mostrar la scrollbar
    for i in range(100):
        text_area.insert(tk.END, f"Línea {i + 1}\n")

def crear_graficos(frame):
    # Gráfico de Calorías por hora (últimas 3 horas)
    horas = [(datetime.now() - timedelta(hours=i)).strftime('%H:%M') for i in range(3)]
    calorias_horas = [random.randint(50, 150) for _ in range(3)]  # Datos simulados para calorías por hora

    # Frame para el gráfico horario con color de fondo
    frame_horas = tk.Frame(frame, bg='#FFDAB9')  # Light peach background
    frame_horas.grid(row=0, column=0, padx=5, pady=5)

    fig_horas, ax_horas = plt.subplots(figsize=(2.9, 2.5))
    ax_horas.bar(horas, calorias_horas, color='orange')
    ax_horas.set_title('Calorías por Hora')
    ax_horas.set_xlabel('Horas')
    ax_horas.set_ylabel('Calorías')
    ax_horas.set_xticks(horas)
    ax_horas.set_xticklabels(horas, rotation=45)

    # Crear el canvas para el gráfico horario
    canvas_horas = FigureCanvasTkAgg(fig_horas, master=frame_horas)
    canvas_horas.get_tk_widget().grid(row=0, column=0, sticky='nsew')

    # Gráfico de Calorías Semanales con color de fondo
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    calorias_semanales = [random.randint(1500, 3000) for _ in dias_semana]  # Datos simulados para la semana

    frame_semanal = tk.Frame(frame, bg='#FFB6C1')  # Light pink background
    frame_semanal.grid(row=1, column=0, padx=5, pady=5)

    fig_semanal, ax_semanal = plt.subplots(figsize=(2.9, 2.5))
    ax_semanal.bar(dias_semana, calorias_semanales, color='orange')
    ax_semanal.set_title('Calorías Semanales')
    ax_semanal.set_xlabel('Días de la Semana')
    ax_semanal.set_ylabel('Calorías')

    canvas_semanal = FigureCanvasTkAgg(fig_semanal, master=frame_semanal)
    canvas_semanal.get_tk_widget().grid(row=1, column=0, sticky='nsew')

    # Gráfico de Calorías Mensuales con color de fondo
    dias_mes = [str(i) for i in range(1, 31)]
    calorias_mensuales = [random.randint(1500, 3000) for _ in range(30)]  # Datos simulados para el mes

    frame_mensual = tk.Frame(frame, bg='#E6E6FA')  # Lavender background
    frame_mensual.grid(row=2, column=0, padx=5, pady=5)

    fig_mensual, ax_mensual = plt.subplots(figsize=(2.9, 2.5))
    ax_mensual.bar(dias_mes, calorias_mensuales, color='orange')
    ax_mensual.set_title('Calorías Mensuales')
    ax_mensual.set_xlabel('Días del Mes')
    ax_mensual.set_ylabel('Calorías')
    ax_mensual.set_xticks(dias_mes[::5])
    ax_mensual.set_xticklabels(dias_mes[::5], rotation=45)

    canvas_mensual = FigureCanvasTkAgg(fig_mensual, master=frame_mensual)
    canvas_mensual.get_tk_widget().grid(row=2, column=0, sticky='nsew')
