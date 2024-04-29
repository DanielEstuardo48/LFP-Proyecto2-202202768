import tkinter as tk
from tkinter import ttk
#from Estilos import *

win = tk.Tk()
win.title('Menu Principal')
window_width = 650  # Ancho de la ventana
window_height = 550
screen_width = win.winfo_screenwidth()  # Ancho de la pantalla
screen_height = win.winfo_screenheight()  # Altura de la pantalla
x_coordinate = (screen_width - window_width) // 2  # Coordenada x para centrar la ventana
y_coordinate = (screen_height - window_height) // 2  # Coordenada y para centrar la ventana
win.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")  # Establecer la geometría de la ventana
win.configure(bg="#f0f0f0")

# ========================= Estilos ========================= 
# Estilo de botones
style_btn = ttk.Style()
style_btn.configure("Round.TButton", foreground="black", background="#3A85FF", font=("Comic Sans MS", 12), borderwidth=0)

#! Apartado de pestañas
pestanas = ttk.Notebook(win)

# Pestaña de archivo
Archivo = ttk.Frame(pestanas)
btn_guardar = ttk.Button(Archivo, text="Guardar", style='Round.TButton')
btn_guardar.pack()
Analisis = ttk.Frame(pestanas)

pestanas.add(Archivo, text='Archivo')
pestanas.add(Analisis, text='Analisis')

pestanas.pack(expand=1, fill = 'both')

win.mainloop()