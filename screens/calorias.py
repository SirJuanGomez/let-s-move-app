import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
from configuracion.api import *

def interfaz_calorias(ventana):
    # Crear un frame principal para contener los gráficos y la scrollbar
    frame_principal = tk.Frame(ventana)
    frame_principal.grid(row=0, column=0, sticky='nsew')

    # Crear un canvas que contendrá los gráficos
    canvas = tk.Canvas(frame_principal)
    canvas.grid(row=0, column=0, sticky='nsew')

    # Crear un scrollbar
    scrollbar = tk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # Configurar el canvas para usar la scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Crear un segundo frame que se colocará en el canvas
    frame_graficos = tk.Frame(canvas)

    # Crear una ventana en el canvas para el segundo frame
    canvas.create_window((0, 0), window=frame_graficos, anchor='nw')

    def crear_graficos(frame):
        # Gráfico de Calorías por hora (últimas 3 horas)
        horas = [(datetime.now() - timedelta(hours=i)).strftime('%H:%M') for i in range(3)]
        calorias_horas = [get_calories('today')] * 3  # Reemplazar con datos reales si están disponibles

        # Frame para el gráfico horario
        frame_horas = tk.Frame(frame)
        frame_horas.grid(row=0, column=0, padx=5, pady=5)

        fig_horas, ax_horas = plt.subplots(figsize=(2.9, 2.5))
        ax_horas.bar(horas, calorias_horas, color='orange')
        ax_horas.set_title('Calorías por Hora')
        ax_horas.set_xlabel('Horas')
        ax_horas.set_ylabel('Calorías')
        ax_horas.set_xticks(horas)
        ax_horas.set_xticklabels(horas, rotation=45)

        canvas_horas = FigureCanvasTkAgg(fig_horas, master=frame_horas)
        canvas_horas.draw()
        canvas_horas.grid(row=0, column=0, sticky='nsew')

        # Gráfico de Calorías Semanales
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        calorias_semanales = get_calories_week()

        # Frame para el gráfico semanal
        frame_semanal = tk.Frame(frame)
        frame_semanal.grid(row=1, column=0, padx=5, pady=5)

        fig_semanal, ax_semanal = plt.subplots(figsize=(2.9, 2.5))
        ax_semanal.bar(dias_semana, calorias_semanales, color='orange')
        ax_semanal.set_title('Calorías Semanales')
        ax_semanal.set_xlabel('Días de la Semana')
        ax_semanal.set_ylabel('Calorías')

        canvas_semanal = FigureCanvasTkAgg(fig_semanal, master=frame_semanal)
        canvas_semanal.draw()
        canvas_semanal.grid(row=0, column=0, sticky='nsew')

        # Gráfico de Calorías Mensuales
        dias_mes = [str(i) for i in range(1, 31)]
        calorias_mensuales = get_calories_month()

        # Frame para el gráfico mensual
        frame_mensual = tk.Frame(frame)
        frame_mensual.grid(row=2, column=0, padx=5, pady=5)

        fig_mensual, ax_mensual = plt.subplots(figsize=(2.9, 2.5))
        ax_mensual.bar(dias_mes, calorias_mensuales, color='orange')
        ax_mensual.set_title('Calorías Mensuales')
        ax_mensual.set_xlabel('Días del Mes')
        ax_mensual.set_ylabel('Calorías')
        ax_mensual.set_xticks(dias_mes[::5])
        ax_mensual.set_xticklabels(dias_mes[::5], rotation=45)

        canvas_mensual = FigureCanvasTkAgg(fig_mensual, master=frame_mensual)
        canvas_mensual.draw()
        canvas_mensual.grid(row=0, column=0, sticky='nsew')

        # Actualizar el tamaño del canvas para que encaje en el frame
        frame_graficos.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    crear_graficos(frame_graficos)

    # Ajustar el tamaño de la ventana
    ventana.grid_rowconfigure(0, weight=1)  # Permitir que el canvas se expanda