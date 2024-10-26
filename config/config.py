# config.py
import tkinter as tk

def set_placeholder(entry, placeholder):
    """Configura el marcador de posición para un campo de entrada."""
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="grey")

def clear_placeholder(entry, placeholder):
    """Limpia el marcador de posición en el campo de entrada."""
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black")

# Placeholders para los campos de registro
placeholders = {
    "email": "example@example.com",
    "password": "********",
    "username": "username",
    "nombre": "nombre",
    "apellido": "apellido"
}
