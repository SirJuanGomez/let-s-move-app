def crear_graficos_calorias(frame):
    # Gráfico 1: Calorías diarias (últimas 3 horas)
    horas = [(datetime.now() - timedelta(hours=i)).strftime('%H:%M') for i in range(3)]
    calorias_horas = [get_calories('today')] * 3  # Reemplazar con datos reales si están disponibles

    # Frame para el gráfico horario
    frame_horas = Frame(frame)
    frame_horas.pack(pady=10)

    fig_horas, ax_horas = plt.subplots(figsize=(5, 3))
    ax_horas.bar(horas, calorias_horas, color='orange')
    ax_horas.set_title('Calorías de las Últimas 3 Horas')
    ax_horas.set_xlabel('Horas')
    ax_horas.set_ylabel('Calorías')
    ax_horas.set_xticks(horas)
    ax_horas.set_xticklabels(horas, rotation=45)

    canvas_horas = FigureCanvasTkAgg(fig_horas, master=frame_horas)
    canvas_horas.draw()
    canvas_horas.get_tk_widget().pack()

    # Gráfico 2: Calorías semanales
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    calorias_semanales = get_calories_week()  # Obtener calorías de la semana

    # Frame para el gráfico semanal
    frame_semanal = Frame(frame)
    frame_semanal.pack(pady=10)

    fig_semanal, ax_semanal = plt.subplots(figsize=(5, 3))
    ax_semanal.bar(dias_semana, calorias_semanales, color='orange')
    ax_semanal.set_title('Calorías Semanales')
    ax_semanal.set_xlabel('Días de la Semana')
    ax_semanal.set_ylabel('Calorías')

    canvas_semanal = FigureCanvasTkAgg(fig_semanal, master=frame_semanal)
    canvas_semanal.draw()
    canvas_semanal.get_tk_widget().pack()

    # Gráfico 3: Calorías mensuales
    dias_mes = [str(i) for i in range(1, 31)]
    calorias_mensuales = get_calories_month()  # Obtener calorías del mes

    # Frame para el gráfico mensual
    frame_mensual = Frame(frame)
    frame_mensual.pack(pady=10)

    fig_mensual, ax_mensual = plt.subplots(figsize=(5, 3))
    ax_mensual.bar(dias_mes, calorias_mensuales, color='orange')
    ax_mensual.set_title('Calorías Mensuales')
    ax_mensual.set_xlabel('Días del Mes')
    ax_mensual.set_ylabel('Calorías')
    ax_mensual.set_xticks(dias_mes[::5])  # Mostrar solo algunos días en el eje X
    ax_mensual.set_xticklabels(dias_mes[::5], rotation=45)

    canvas_mensual = FigureCanvasTkAgg(fig_mensual, master=frame_mensual)
    canvas_mensual.draw()
    canvas_mensual.get_tk_widget().pack()
