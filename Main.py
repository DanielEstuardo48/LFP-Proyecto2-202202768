import tkinter as tk
from tkinter import ttk, filedialog
import AnalizadorSintactico
from Funciones import *

#Variables para almacenar datos del archivo cargado
archivo = ""
datos = ""

#Parte del codigo de funciones
def abrir_archivo():
    global archivo
    archivo = filedialog.askopenfilename(initialdir="C:/Users/danis/OneDrive/Documents/Quinto Semestre/LFP/[LFP]Proyecto2", title="Explorador")
    if archivo:
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                global datos
                datos = file.read()  # Leer el contenido del archivo
                texto.delete(1.0, tk.END)  # Limpiar el widget de texto
                texto.insert(tk.END, datos)  # Insertar los datos en el widget de texto
                AnalizadorSintactico.intruccion(datos)
        except Exception as e:
            print("Error al cargar archivo:", e)

def guardar_archivo():
    global archivo
    if archivo:
        try:
            with open(archivo, 'w', encoding='utf-8') as file:
                contenido = texto.get(1.0, tk.END)
                file.write(contenido)
            print("Archivo guardado :)")
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, "Archivo guardado :)")
        except Exception as e:
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, e)
            print("Error al guardar el archivo :( :", e)
    else:
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, "No se ha cargado ningun archivo :v ")
        print("No se ha cargado ningun archivo :v ")

def limpiar_texto():
    texto.delete(1.0, tk.END)

def guardar_como():
    global archivo
    contenido = texto.get(1.0, tk.END)
    archivo = filedialog.asksaveasfilename(defaultextension=".lfp", filetypes=[("Archivos de texto", "*.lfp"), ("Todos los archivos", "*.*")])
    if archivo:
        try:
            with open(archivo, 'w', encoding='utf-8') as file:
                file.write(contenido)
            print("Archivo guardado exitosamente.")
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, "Archivo guardado :)")
        except Exception as e:
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, e)
            print("Error al guardar archivo:", e)

def cerrar_aplicacion():
    win.quit()


def mostrar_resultados():
    resultado_instrucciones = AnalizadorSintactico.operar_()

    for instruccion in resultado_instrucciones:
        if isinstance(instruccion, CrearDB):
            print(instruccion.ejecutarT())
        elif isinstance(instruccion, EliminarDB):
            print(instruccion.ejecutarT())
        elif isinstance(instruccion, CrearColeccion):
            print(instruccion.ejecutarT())
        else:
            print("El resultado no es una instancia de CrearDB, EliminarDB o CrearColeccion:", instruccion)

#Parte de Tkinter
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
btn_abrir = ttk.Button(Archivo, text="Abrir", command=abrir_archivo)
btn_abrir.place(x=10, y=10)
btn_guardar = ttk.Button(Archivo, text="Guardar", command=guardar_archivo)
btn_guardar.place(x=btn_abrir.winfo_reqwidth() + 15, y=10)
btn_nuevo = ttk.Button(Archivo, text="Nuevo", command=limpiar_texto)
btn_nuevo.place(x=btn_guardar.winfo_reqwidth() + 95, y=10)
btn_guardarc = ttk.Button(Archivo, text="Guardar como", command=guardar_como)
btn_guardarc.place(x=btn_nuevo.winfo_reqwidth() + 175, y=10)
btn_Salir = ttk.Button(Archivo, text="Salir", command=cerrar_aplicacion)
btn_Salir.place(x=btn_guardar.winfo_reqwidth() + 475, y=10)
# Crear un Text debajo de los botones
texto_frame = tk.Frame(Archivo)
texto_frame.place(x=10, y=50, relwidth=1, relheight=0.8)


texto = tk.Text(texto_frame, bg="white", bd=0, wrap="word")
scrollbar = ttk.Scrollbar(texto_frame, orient="vertical", command=texto.yview)
texto.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
texto.pack(side="left", fill="both", expand=True)
texto.insert(tk.END, "--- Area de edicion de codigo\n")  # Insertar los datos en el widget de texto

#! Pestaña de analizadores :/
Analisis = ttk.Frame(pestanas)
btn_traducir = ttk.Button(Analisis, text="Traducir", command=mostrar_resultados)
btn_traducir.place(x=10, y=10)

# Crear un Text debajo de los botones
texto_frame2 = tk.Frame(Analisis)
texto_frame2.place(x=10, y=50, relwidth=1, relheight=0.8)


texto2 = tk.Text(texto_frame2, bg="white", bd=0, wrap="word")
scrollbar2 = ttk.Scrollbar(texto_frame2, orient="vertical", command=texto2.yview)
texto2.configure(yscrollcommand=scrollbar2.set)

scrollbar2.pack(side="right", fill="y")
texto2.pack(side="left", fill="both", expand=True)
texto2.insert(tk.END, "--- Aqui se mostrara el texto traducido :) ---\n")


pestanas.add(Archivo, text='Archivo')
pestanas.add(Analisis, text='Analisis')

pestanas.pack(expand=1, fill = 'both')

win.mainloop()