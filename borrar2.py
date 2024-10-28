import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
from tkinter import Tk, Frame, Scrollbar, Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para crear los gráficos
def crear_graficos(frame):
    # Gráfico 1: Valores por las últimas 3 horas
    hora_actual = datetime.now()
    horas = [(hora_actual - timedelta(hours=i)).strftime('%H:%M') for i in range(3)]
    valores_horas = np.random.randint(0, 30, size=3)

    # Frame para el gráfico horario
    frame_horas = Frame(frame)
    frame_horas.pack(pady=10)

    fig_horas, ax_horas = plt.subplots(figsize=(5, 3))
    ax_horas.bar(horas, valores_horas, color='lightgreen')
    ax_horas.set_title('Valores de las Últimas 3 Horas')
    ax_horas.set_xlabel('Horas')
    ax_horas.set_ylabel('Valores')
    ax_horas.set_xticks(horas)
    ax_horas.set_xticklabels(horas, rotation=45)

    # Integrar Matplotlib con Tkinter
    canvas_horas = FigureCanvasTkAgg(fig_horas, master=frame_horas)
    canvas_horas.draw()
    canvas_horas.get_tk_widget().pack()

    # Gráfico 2: Valores semanales
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    valores_semanales = [10, 15, 7, 20, 12, 8, 5]

    # Frame para el gráfico semanal
    frame_semanal = Frame(frame)
    frame_semanal.pack(pady=10)

    fig_semanal, ax_semanal = plt.subplots(figsize=(5, 3))
    ax_semanal.bar(dias_semana, valores_semanales, color='skyblue')
    ax_semanal.set_title('Valores Semanales')
    ax_semanal.set_xlabel('Días de la Semana')
    ax_semanal.set_ylabel('Valores')

    # Integrar Matplotlib con Tkinter
    canvas_semanal = FigureCanvasTkAgg(fig_semanal, master=frame_semanal)
    canvas_semanal.draw()
    canvas_semanal.get_tk_widget().pack()

    # Gráfico 3: Valores mensuales
    dias_mes = [str(i) for i in range(1, 31)]
    valores_mensuales = np.random.randint(5, 20, size=30)

    # Frame para el gráfico mensual
    frame_mensual = Frame(frame)
    frame_mensual.pack(pady=10)

    fig_mensual, ax_mensual = plt.subplots(figsize=(5, 3))
    ax_mensual.bar(dias_mes, valores_mensuales, color='salmon')
    ax_mensual.set_title('Valores Mensuales')
    ax_mensual.set_xlabel('Días del Mes')
    ax_mensual.set_ylabel('Valores')
    ax_mensual.set_xticks(dias_mes[::5])
    ax_mensual.set_xticklabels(dias_mes[::5], rotation=45)

    # Integrar Matplotlib con Tkinter
    canvas_mensual = FigureCanvasTkAgg(fig_mensual, master=frame_mensual)
    canvas_mensual.draw()
    canvas_mensual.get_tk_widget().pack()

# Crear la ventana principal
root = Tk()
root.title("Gráficos con Deslizador")
root.geometry("600x400")  # Ventana más pequeña

# Crear un marco y un lienzo para el scroll
frame = Frame(root)
frame.pack(fill='both', expand=True)

canvas = Canvas(frame)
canvas.pack(side='left', fill='both', expand=True)

scrollbar = Scrollbar(frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')

canvas.configure(yscrollcommand=scrollbar.set)

# Crear un marco para contener los gráficos
marco_graficos = Frame(canvas)
canvas.create_window((0, 0), window=marco_graficos, anchor='nw')

# Crear los gráficos en el marco
crear_graficos(marco_graficos)

# Configurar el scroll para el lienzo
marco_graficos.update_idletasks()  # Actualiza el tamaño del marco
canvas.config(scrollregion=canvas.bbox("all"))  # Establecer la región de desplazamiento

# Ejecutar la aplicación
root.mainloop()
