import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Ejemplo de Scrollbar")
    root.geometry("292x543")  # Establecer el tamaño de la ventana

    # Crear un marco para contener el texto y la scrollbar
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Crear un widget de texto con un scrollbar
    text_area = tk.Text(frame, wrap='word')
    scrollbar = tk.Scrollbar(frame, command=text_area.yview)
    text_area.config(yscrollcommand=scrollbar.set)

    # Empaquetar los widgets
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Agregar algo de texto para mostrar la scrollbar
    for i in range(50):
        text_area.insert(tk.END, f"Línea {i + 1}\n")

    root.mainloop()

if __name__ == "__main__":
    main()
