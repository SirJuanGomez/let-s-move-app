import tkinter as tk  # Importa la biblioteca tkinter para crear interfaces gráficas
import matplotlib.pyplot as plt  # Importa matplotlib para crear gráficos
from configuracion.api import *  # Importa funciones y clases de un módulo personalizado (no especificado aquí)
from configuracion.utils import *  # Importa utilidades de otro módulo personalizado
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Permite integrar gráficos de Matplotlib en Tkinter
from PIL import Image, ImageTk  # Importa módulos de PIL para manipulación de imágenes
import os  # Proporciona funciones para interactuar con el sistema operativo

# Diccionario con placeholders para los campos de entrada del usuario
placeholders = {
    "email": "Ingresa tu email",  # Placeholder para el campo de email
    "password": "Ingresa tu contraseña",  # Placeholder para el campo de contraseña
    "username": "Ingresa tu nombre de usuario",  # Placeholder para el campo de nombre de usuario
    "nombre": "Ingresa tu nombre",  # Placeholder para el campo de nombre
    "apellido": "Ingresa tu apellido"  # Placeholder para el campo de apellido
}

# Función para cargar una imagen desde una ruta especificada
def cargar_imagen(ruta_imagen, tamano):
    try:
        imagen = Image.open(ruta_imagen)  # Intenta abrir la imagen desde la ruta
        imagen = imagen.resize(tamano, Image.LANCZOS)  # Redimensiona la imagen al tamaño especificado usando LANCZOS
        return ImageTk.PhotoImage(imagen)  # Devuelve la imagen redimensionada en formato Tkinter
    except Exception as e:  # Captura cualquier excepción
        print(f"Error al cargar la imagen: {e}")  # Imprime un mensaje de error
        return None  # Devuelve None si hay un error

# Función para aplicar un efecto de transparencia a un color
def aplicar_alpha(color, alpha):
    r, g, b = color  # Descompone el color en componentes RGB
    # Calcula el nuevo valor de cada componente basado en el valor de alpha
    r = int((1 - alpha) * 255 + alpha * r)  # Mezcla el componente rojo
    g = int((1 - alpha) * 255 + alpha * g)  # Mezcla el componente verde
    b = int((1 - alpha) * 255 + alpha * b)  # Mezcla el componente azul
    
    # Devuelve el nuevo color en formato hexadecimal
    return f'#{r:02x}{g:02x}{b:02x}'  

def set_placeholder(entry, placeholder):
    """Establece un placeholder en el campo de entrada."""
    # Verifica si el campo de entrada está vacío
    if entry.get() == "":
        entry.insert(0, placeholder)  # Inserta el texto del placeholder en el campo
        entry.config(fg="grey")  # Cambia el color del texto a gris para indicar que es un placeholder

def clear_placeholder(entry, placeholder):
    """Limpia el placeholder cuando el campo recibe el foco."""
    # Verifica si el texto actual del campo es igual al placeholder
    if entry.get() == placeholder:
        entry.delete(0, tk.END)  # Limpia el campo de entrada
        entry.config(fg="black")  # Cambia el color del texto a negro para indicar que es entrada válida

def volver(ventana, main):
    """Limpia la ventana y vuelve a la pantalla principal."""
    # Itera sobre todos los widgets en la ventana
    for widget in ventana.winfo_children():
        widget.destroy()  # Elimina cada widget de la ventana
    main()  # Llama a la función main para mostrar la pantalla principal


def crear_graficos_calorias(frame, graph_type):
    # Limpiar gráficos anteriores
    for widget in frame.winfo_children():
        widget.destroy()  # Elimina todos los widgets hijos del frame para limpiar la vista

    # Etiqueta para el título de las gráficas
    label_titulo = tk.Label(frame, text='Gráficas Calorías', font=('Arial', 16, 'bold'))
    label_titulo.grid(row=0, column=0, padx=5, pady=5)  # Coloca la etiqueta en la cuadrícula

    # Frame contenedor para el Canvas
    frame_canvas = tk.Frame(frame)
    frame_canvas.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')  # Coloca el frame para el canvas en la cuadrícula

    # Configura el peso de la columna y la fila para que se expandan correctamente
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Canvas para los gráficos
    canvas = tk.Canvas(frame_canvas)
    canvas.pack(fill=tk.BOTH, expand=True)  # Ajusta el canvas para llenar el frame

    # Configuración del tamaño del gráfico
    fig_width = 7  # Ancho del gráfico en pulgadas
    fig_height = 5  # Altura del gráfico en pulgadas

    # Crear gráficos según el tipo especificado
    if graph_type == "Hoy":
        # Genera las horas del día para las últimas 3 horas
        horas = [(datetime.now() - timedelta(hours=i)).strftime('%H:%M') for i in range(3)][::-1]
        calorias_horas = [get_calories('today')] * 3  # Obtiene las calorías consumidas hoy

        # Crea el gráfico de barras para calorías por hora
        fig_horas, ax_horas = plt.subplots(figsize=(fig_width, fig_height))
        ax_horas.bar(horas, calorias_horas, color='orange', width=0.4)  # Crea el gráfico de barras
        ax_horas.set_title('Calorías por Hora', fontsize=16)  # Establece el título
        ax_horas.set_xlabel('Horas', fontsize=14)  # Etiqueta del eje X
        ax_horas.set_ylabel('Calorías', fontsize=14)  # Etiqueta del eje Y
        ax_horas.set_xticks(horas)  # Establece las marcas en el eje X
        ax_horas.set_xticklabels(horas, rotation=90, ha='right', fontsize=10)  # Rotación de las etiquetas
        ax_horas.set_ylim(0, max(calorias_horas) + 10)  # Establece el límite del eje Y

    elif graph_type == "Semana":
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']  # Días de la semana
        calorias_semanales = get_calories_week()  # Obtiene las calorías consumidas esta semana

        # Crea el gráfico de barras para calorías por día de la semana
        fig_semanal, ax_semanal = plt.subplots(figsize=(fig_width, fig_height))
        ax_semanal.bar(dias_semana, calorias_semanales, color='orange', width=0.4)
        ax_semanal.set_title('Calorías Semanales', fontsize=16)
        ax_semanal.set_xlabel('Días de la Semana', fontsize=14)
        ax_semanal.set_ylabel('Calorías', fontsize=14)
        ax_semanal.set_xticklabels(dias_semana, rotation=90, ha='right', fontsize=10)
        ax_semanal.set_ylim(0, max(calorias_semanales) + 10)  # Establece el límite del eje Y

    elif graph_type == "Mes":
        dias_mes = [f'Día {i + 1}' for i in range(30)]  # Días del mes (suponiendo un mes de 30 días)
        calorias_mensuales = get_calories_month()  # Obtiene las calorías consumidas este mes

        # Crea el gráfico de barras para calorías por día del mes
        fig_mensual, ax_mensual = plt.subplots(figsize=(fig_width, fig_height))
        ax_mensual.bar(dias_mes, calorias_mensuales[:30], color='orange', width=0.4)
        ax_mensual.set_title('Calorías Mensuales', fontsize=16)
        ax_mensual.set_xlabel('Días del Mes', fontsize=14)
        ax_mensual.set_ylabel('Calorías', fontsize=14)
        ax_mensual.set_xticks(dias_mes[::5])  # Muestra cada 5 días en el eje X
        ax_mensual.set_xticklabels(dias_mes[::5], rotation=90, ha='right', fontsize=10)
        ax_mensual.set_ylim(0, max(calorias_mensuales[:30]) + 10)  # Establece el límite del eje Y

    # Ajustar los márgenes específicos del gráfico
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

    # Mostrar el gráfico en el canvas
    canvas_grafico = FigureCanvasTkAgg(fig_horas if graph_type == "Hoy" else fig_semanal if graph_type == "Semana" else fig_mensual, master=canvas)
    canvas_grafico.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Añade el gráfico al canvas

def crear_graficos_pasos(frame, graph_type):
    # Limpiar gráficos anteriores
    for widget in frame.winfo_children():
        widget.destroy()  # Elimina todos los widgets hijos del frame para limpiar la vista

    # Etiqueta para el título de las gráficas
    label_titulo = tk.Label(frame, text='Gráficas Pasos', font=('Arial', 16, 'bold'))
    label_titulo.grid(row=0, column=0, padx=5, pady=5)  # Coloca la etiqueta en la cuadrícula

    # Frame contenedor para el Canvas
    frame_canvas = tk.Frame(frame)
    frame_canvas.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')  # Coloca el frame para el canvas en la cuadrícula

    # Configura el peso de la columna y la fila para que se expandan correctamente
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Canvas para los gráficos
    canvas = tk.Canvas(frame_canvas)
    canvas.pack(fill=tk.BOTH, expand=True)  # Ajusta el canvas para llenar el frame

    # Configuración del tamaño del gráfico
    fig_width = 7  # Ancho del gráfico en pulgadas
    fig_height = 5  # Altura del gráfico en pulgadas

    # Crear gráficos según el tipo especificado
    if graph_type == "Hoy":
        # Genera las horas del día para las últimas 3 horas
        horas = [(datetime.now() - timedelta(hours=i)).strftime('%H:%M') for i in range(3)][::-1]
        pasos_horas = [get_steps('today')] * 3  # Obtiene los pasos dados hoy

        # Crea el gráfico de barras para pasos por hora
        fig_horas, ax_horas = plt.subplots(figsize=(fig_width, fig_height))
        ax_horas.bar(horas, pasos_horas, color='blue', width=0.4)  # Crea el gráfico de barras
        ax_horas.set_title('Pasos por Hora', fontsize=16)  # Establece el título
        ax_horas.set_xlabel('Horas', fontsize=14)  # Etiqueta del eje X
        ax_horas.set_ylabel('Pasos', fontsize=14)  # Etiqueta del eje Y
        ax_horas.set_xticks(horas)  # Establece las marcas en el eje X
        ax_horas.set_xticklabels(horas, rotation=90, ha='right', fontsize=10)  # Rotación de las etiquetas
        ax_horas.set_ylim(0, max(pasos_horas) + 10)  # Establece el límite del eje Y

    elif graph_type == "Semana":
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']  # Días de la semana
        pasos_semanales = get_steps_week()  # Obtiene los pasos dados esta semana

        # Crea el gráfico de barras para pasos por día de la semana
        fig_semanal, ax_semanal = plt.subplots(figsize=(fig_width, fig_height))
        ax_semanal.bar(dias_semana, pasos_semanales, color='blue', width=0.4)
        ax_semanal.set_title('Pasos Semanales', fontsize=16)
        ax_semanal.set_xlabel('Días de la Semana', fontsize=14)
        ax_semanal.set_ylabel('Pasos', fontsize=14)
        ax_semanal.set_xticklabels(dias_semana, rotation=90, ha='right', fontsize=10)
        ax_semanal.set_ylim(0, max(pasos_semanales) + 10)  # Establece el límite del eje Y

    elif graph_type == "Mes":
        dias_mes = [f'Día {i + 1}' for i in range(30)]  # Días del mes (suponiendo un mes de 30 días)
        pasos_mensuales = get_steps_month()  # Obtiene los pasos dados este mes

        # Crea el gráfico de barras para pasos por día del mes
        fig_mensual, ax_mensual = plt.subplots(figsize=(fig_width, fig_height))
        ax_mensual.bar(dias_mes, pasos_mensuales[:30], color='blue', width=0.4)
        ax_mensual.set_title('Pasos Mensuales', fontsize=16)
        ax_mensual.set_xlabel('Días del Mes', fontsize=14)
        ax_mensual.set_ylabel('Pasos', fontsize=14)
        ax_mensual.set_xticks(dias_mes[::5])  # Muestra cada 5 días en el eje X
        ax_mensual.set_xticklabels(dias_mes[::5], rotation=90, ha='right', fontsize=10)
        ax_mensual.set_ylim(0, max(pasos_mensuales[:30]) + 10)  # Establece el límite del eje Y

    # Ajustar los márgenes específicos del gráfico
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

    # Mostrar el gráfico en el canvas
    canvas_grafico = FigureCanvasTkAgg(fig_horas if graph_type == "Hoy" else fig_semanal if graph_type == "Semana" else fig_mensual, master=canvas)
    canvas_grafico.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Añade el gráfico al canvas

def crear_graficos_distancia(frame, graph_type):
    # Limpiar gráficos anteriores
    for widget in frame.winfo_children():
        widget.destroy()  # Elimina todos los widgets hijos del frame para limpiar la vista

    # Etiqueta para el título de las gráficas
    label_titulo = tk.Label(frame, text='Gráficas Distancia', font=('Arial', 16, 'bold'))
    label_titulo.grid(row=0, column=0, padx=5, pady=5)  # Coloca la etiqueta en la cuadrícula

    # Frame contenedor para el Canvas
    frame_canvas = tk.Frame(frame)
    frame_canvas.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')  # Coloca el frame para el canvas en la cuadrícula

    # Configura el peso de la columna y la fila para que se expandan correctamente
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # Canvas para los gráficos
    canvas = tk.Canvas(frame_canvas)
    canvas.pack(fill=tk.BOTH, expand=True)  # Ajusta el canvas para llenar el frame

    # Configuración del tamaño del gráfico
    fig_width = 7  # Ancho del gráfico en pulgadas
    fig_height = 5  # Altura del gráfico en pulgadas

    # Crear gráficos según el tipo especificado
    if graph_type == "Hoy":
        # Genera las horas del día para las últimas 3 horas
        horas = [(datetime.now() - timedelta(hours=i)).strftime('%H:%M') for i in range(3)][::-1]
        distancia_horas = [get_distance('today')] * 3  # Obtiene la distancia recorrida hoy

        # Crea el gráfico de barras para distancia por hora
        fig_horas, ax_horas = plt.subplots(figsize=(fig_width, fig_height))
        ax_horas.bar(horas, distancia_horas, color='green', width=0.4)  # Crea el gráfico de barras
        ax_horas.set_title('Distancia por Hora', fontsize=16)  # Establece el título
        ax_horas.set_xlabel('Horas', fontsize=14)  # Etiqueta del eje X
        ax_horas.set_ylabel('Distancia (km)', fontsize=14)  # Etiqueta del eje Y
        ax_horas.set_xticks(horas)  # Establece las marcas en el eje X
        ax_horas.set_xticklabels(horas, rotation=90, ha='right', fontsize=10)  # Rotación de las etiquetas
        ax_horas.set_ylim(0, max(distancia_horas) + 0.5)  # Establece el límite superior del eje Y

    elif graph_type == "Semana":
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']  # Días de la semana
        distancia_semanal = get_distance_week()  # Obtiene la distancia recorrida esta semana

        # Crea el gráfico de barras para distancia por día de la semana
        fig_semanal, ax_semanal = plt.subplots(figsize=(fig_width, fig_height))
        ax_semanal.bar(dias_semana, distancia_semanal, color='green', width=0.4)
        ax_semanal.set_title('Distancia Semanal', fontsize=16)
        ax_semanal.set_xlabel('Días de la Semana', fontsize=14)
        ax_semanal.set_ylabel('Distancia (km)', fontsize=14)
        ax_semanal.set_xticklabels(dias_semana, rotation=90, ha='right', fontsize=10)
        ax_semanal.set_ylim(0, max(distancia_semanal) + 0.5)  # Establece el límite superior del eje Y

    elif graph_type == "Mes":
        dias_mes = [f'Día {i + 1}' for i in range(30)]  # Días del mes (suponiendo un mes de 30 días)
        distancia_mensual = get_distance_month()  # Obtiene la distancia recorrida este mes

        # Crea el gráfico de barras para distancia por día del mes
        fig_mensual, ax_mensual = plt.subplots(figsize=(fig_width, fig_height))
        ax_mensual.bar(dias_mes, distancia_mensual[:30], color='green', width=0.4)
        ax_mensual.set_title('Distancia Mensual', fontsize=16)
        ax_mensual.set_xlabel('Días del Mes', fontsize=14)
        ax_mensual.set_ylabel('Distancia (km)', fontsize=14)
        ax_mensual.set_xticks(dias_mes[::5])  # Muestra cada 5 días en el eje X
        ax_mensual.set_xticklabels(dias_mes[::5], rotation=90, ha='right', fontsize=10)
        ax_mensual.set_ylim(0, max(distancia_mensual[:30]) + 0.5)  # Establece el límite superior del eje Y

    # Ajustar los márgenes específicos del gráfico
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

    # Mostrar el gráfico en el canvas
    canvas_grafico = FigureCanvasTkAgg(fig_horas if graph_type == "Hoy" else fig_semanal if graph_type == "Semana" else fig_mensual, master=canvas)
    canvas_grafico.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Añade el gráfico al canvas

def crear_graficos_combinados(graph_type):
    # Configuración del tamaño del gráfico
    fig_width = 15  # Ancho en pulgadas
    fig_height = 10  # Altura en pulgadas
    fig, axs = plt.subplots(3, 1, figsize=(fig_width, fig_height), sharex=True)  # Crea una figura con 3 subgráficas verticales

    # Crear gráficos según el tipo especificado
    if graph_type == "Hoy":
        # Genera las horas del día para las últimas 3 horas
        horas = [(datetime.now() - timedelta(hours=i)).strftime('%H:%M') for i in range(3)][::-1]
        # Obtiene datos de calorías, pasos y distancia para hoy
        calorias_horas = [get_calories('today')] * 3
        pasos_horas = [get_steps('today')] * 3
        distancia_horas = [get_distance('today')] * 3
        
        # Gráfica de Calorías
        axs[0].bar(horas, calorias_horas, color='orange', width=0.4)  # Crea un gráfico de barras
        axs[0].set_title('Calorías por Hora', fontsize=16)  # Establece el título
        axs[0].set_ylabel('Calorías', fontsize=14)  # Etiqueta del eje Y
        axs[0].set_ylim(0, max(calorias_horas) + 10)  # Establece el límite superior del eje Y

        # Gráfica de Pasos
        axs[1].bar(horas, pasos_horas, color='blue', width=0.4)
        axs[1].set_title('Pasos por Hora', fontsize=16)
        axs[1].set_ylabel('Pasos', fontsize=14)
        axs[1].set_ylim(0, max(pasos_horas) + 10)

        # Gráfica de Distancia
        axs[2].bar(horas, distancia_horas, color='green', width=0.4)
        axs[2].set_title('Distancia por Hora', fontsize=16)
        axs[2].set_ylabel('Distancia (km)', fontsize=14)
        axs[2].set_ylim(0, max(distancia_horas) + 0.5)

    elif graph_type == "Semana":
        # Días de la semana para la gráfica
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        # Obtiene datos de calorías, pasos y distancia para la semana
        calorias_semanales = get_calories_week()
        pasos_semanales = get_steps_week()
        distancia_semanal = get_distance_week()
        
        # Gráfica de Calorías
        axs[0].bar(dias_semana, calorias_semanales, color='orange', width=0.4)
        axs[0].set_title('Calorías Semanales', fontsize=16)
        axs[0].set_ylabel('Calorías', fontsize=14)
        axs[0].set_ylim(0, max(calorias_semanales) + 10)

        # Gráfica de Pasos
        axs[1].bar(dias_semana, pasos_semanales, color='blue', width=0.4)
        axs[1].set_title('Pasos Semanales', fontsize=16)
        axs[1].set_ylabel('Pasos', fontsize=14)
        axs[1].set_ylim(0, max(pasos_semanales) + 10)

        # Gráfica de Distancia
        axs[2].bar(dias_semana, distancia_semanal, color='green', width=0.4)
        axs[2].set_title('Distancia Semanal', fontsize=16)
        axs[2].set_ylabel('Distancia (km)', fontsize=14)
        axs[2].set_ylim(0, max(distancia_semanal) + 0.5)

    elif graph_type == "Mes":
        # Días del mes (suponiendo un mes de 30 días)
        dias_mes = [f'Día {i + 1}' for i in range(30)]
        # Obtiene datos de calorías, pasos y distancia para el mes
        calorias_mensuales = get_calories_month()
        pasos_mensuales = get_steps_month()
        distancia_mensual = get_distance_month()
        
        # Gráfica de Calorías
        axs[0].bar(dias_mes, calorias_mensuales[:30], color='orange', width=0.4)
        axs[0].set_title('Calorías Mensuales', fontsize=16)
        axs[0].set_ylabel('Calorías', fontsize=14)
        axs[0].set_ylim(0, max(calorias_mensuales[:30]) + 10)

        # Gráfica de Pasos
        axs[1].bar(dias_mes, pasos_mensuales[:30], color='blue', width=0.4)
        axs[1].set_title('Pasos Mensuales', fontsize=16)
        axs[1].set_ylabel('Pasos', fontsize=14)
        axs[1].set_ylim(0, max(pasos_mensuales[:30]) + 10)

        # Gráfica de Distancia
        axs[2].bar(dias_mes, distancia_mensual[:30], color='green', width=0.4)
        axs[2].set_title('Distancia Mensual', fontsize=16)
        axs[2].set_ylabel('Distancia (km)', fontsize=14)
        axs[2].set_ylim(0, max(distancia_mensual[:30]) + 0.5)

    # Configuración de etiquetas en el eje x para todas las subgráficas
    for ax in axs:
        ax.set_xticks(ax.get_xticks())  # Obtiene las marcas actuales del eje X
        ax.set_xticklabels(ax.get_xticks(), rotation=90, ha='right', fontsize=10)  # Ajusta la rotación y el formato de las etiquetas

    # Ajustar los márgenes específicos del gráfico
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

    # Ruta donde se guardarán los gráficos
    grafica_folder = 'img/img_graficas'
    if not os.path.exists(grafica_folder):
        os.makedirs(grafica_folder)  # Crea la carpeta si no existe

    # Guardar la figura como imagen JPG en la carpeta especificada
    grafica_path = os.path.join(grafica_folder, f'graficos_combinados_{graph_type.lower()}.jpg')
    plt.savefig(grafica_path, format='jpg')  # Guarda la figura en formato JPG
    plt.close(fig)  # Cierra la figura después de guardar

    return grafica_path  # Devuelve la ruta del gráfico guardado


