import tkinter as tk

def crear_regilla_con_botones_y_frame_adicional():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Regilla de Frames con Botones del Mismo Tamaño y Frame Adicional")

    # Crear el primer frame
    frame1 = tk.Frame(root, width=100, height=100, bg="lightblue")
    frame1.pack_propagate(False)  # Evitar que el frame ajuste su tamaño al contenido
    frame1.grid(row=0, column=0, padx=5, pady=5)  # Usar grid para colocar el frame en la cuadrícula

    # Crear un botón en el primer frame
    boton1 = tk.Button(frame1, text="Botón 1", bg="white", command=lambda: print("Botón 1 presionado"))
    boton1.pack(fill=tk.BOTH, expand=True)  # Llenar el frame y expandir

    # Crear el segundo frame
    frame2 = tk.Frame(root, width=100, height=100, bg="lightgreen")
    frame2.pack_propagate(False)  # Evitar que el frame ajuste su tamaño al contenido
    frame2.grid(row=0, column=1, padx=5, pady=5)  # Colocar en la cuadrícula

    # Crear un botón en el segundo frame
    boton2 = tk.Button(frame2, text="Botón 2", bg="white", command=lambda: print("Botón 2 presionado"))
    boton2.pack(fill=tk.BOTH, expand=True)  # Llenar el frame y expandir

    # Crear el tercer frame
    frame3 = tk.Frame(root, width=100, height=100, bg="lightcoral")
    frame3.pack_propagate(False)  # Evitar que el frame ajuste su tamaño al contenido
    frame3.grid(row=1, column=0, padx=5, pady=5)  # Colocar en la cuadrícula

    # Crear un botón en el tercer frame
    boton3 = tk.Button(frame3, text="Botón 3", bg="white", command=lambda: print("Botón 3 presionado"))
    boton3.pack(fill=tk.BOTH, expand=True)  # Llenar el frame y expandir

    # Crear el cuarto frame
    frame4 = tk.Frame(root, width=100, height=100, bg="lightyellow")
    frame4.pack_propagate(False)  # Evitar que el frame ajuste su tamaño al contenido
    frame4.grid(row=1, column=1, padx=5, pady=5)  # Colocar en la cuadrícula

    # Crear un botón en el cuarto frame
    boton4 = tk.Button(frame4, text="Botón 4", bg="white", command=lambda: print("Botón 4 presionado"))
    boton4.pack(fill=tk.BOTH, expand=True)  # Llenar el frame y expandir

    # Crear un frame adicional debajo de la cuadrícula
    frame_adicional = tk.Frame(root, width=200, height=100, bg="lightgrey")
    frame_adicional.pack_propagate(False)  # Evitar que el frame ajuste su tamaño al contenido
    frame_adicional.grid(row=2, column=0, columnspan=2, padx=5, pady=20)  # Colocar debajo de la cuadrícula

    # Crear botones en el frame adicional
    boton_adicional1 = tk.Button(frame_adicional, text="Botón Adicional 1", bg="white", command=lambda: print("Botón Adicional 1 presionado"))
    boton_adicional1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Llenar el frame y expandir

    boton_adicional2 = tk.Button(frame_adicional, text="Botón Adicional 2", bg="white", command=lambda: print("Botón Adicional 2 presionado"))
    boton_adicional2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Llenar el frame y expandir

    # Ejecutar el bucle principal
    root.mainloop()

# Llamar a la función
crear_regilla_con_botones_y_frame_adicional()
