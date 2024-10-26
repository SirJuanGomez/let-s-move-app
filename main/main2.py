import tkinter as tk

ventana = tk.Tk()
ventana.title("Let's Move")
ventana.geometry("292x543")

def crear_frame(conten_frame, bg_color, width, height, x, y):
    frame = tk.Frame(conten_frame, bg=bg_color, width=width, height=height)
    frame.place(x=x, y=y)
    return frame

def main():
    conten_frame = tk.Frame(ventana, bg="blue", width=292, height=543)
    conten_frame.pack_propagate(False)
    conten_frame.pack()

    # Definir pady, padx, ancho y alto de los botones
    pady_value = 1
    padx_value = 1
    button_width = 15
    button_height = 9

    # Crear todos los frames
    frame_texto = crear_frame(conten_frame, "white", 284, 40, 4, 35)
    tk.Label(frame_texto, text="Bienvenido a Let's Move", bg="white").pack()

    frame_calories = crear_frame(conten_frame, "white", 130, 130, 12, 120)
    tk.Button(frame_calories, text="Calorías", bg="lightgrey", width=button_width, height=button_height).pack(pady=pady_value, padx=padx_value)

    frame_distance = crear_frame(conten_frame, "white", 130, 130, 150, 120)
    tk.Button(frame_distance, text="Distancia", bg="lightgrey", width=button_width, height=button_height).pack(pady=pady_value, padx=padx_value)

    frame_foot = crear_frame(conten_frame, "white", 130, 130, 12, 270)
    tk.Button(frame_foot, text="Paso", bg="lightgrey", width=button_width, height=button_height).pack(pady=pady_value, padx=padx_value)

    frame_registers = crear_frame(conten_frame, "white", 130, 130, 150, 270)
    tk.Button(frame_registers, text="Registros", bg="lightgrey", width=button_width, height=button_height).pack(pady=pady_value, padx=padx_value)

    frame_more = crear_frame(conten_frame, "white", 284, 40,  8, 460)
    tk.Button(frame_more, text="Más", bg="lightgrey", width=38, height=3).pack(pady=pady_value, padx=padx_value)

main()
ventana.mainloop()
