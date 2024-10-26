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

    # Crear todos los frames
    frame_texto = crear_frame(conten_frame, "white", 284, 40, 4, 35)
    tk.Label(frame_texto, text="Bienvenido a Let's Move", bg="white").pack()

    frame_calories = crear_frame(conten_frame, "white", 130, 130, 12, 120)
    frame_distance = crear_frame(conten_frame, "white", 130, 130, 150, 120)
    frame_foot = crear_frame(conten_frame, "white", 130, 130, 12, 270)
    frame_registers = crear_frame(conten_frame, "white", 130, 130, 150, 270)
    frame_more = crear_frame(conten_frame, "white", 284, 40, 4, 460)
main()
ventana.mainloop()
