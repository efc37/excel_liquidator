import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import sys

# Importamos la lógica desde el archivo logic.py
from .logic import calculo_liquidacion, resource_path

# Variables globales para manejar el estado de la selección
archivo_seleccionado = None
nombre_archivo_final = None

def seleccionar(boton_referencia):
    """Abre un diálogo para seleccionar el archivo Excel de entrada."""
    global archivo_seleccionado 
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo de liquidaciones",
        filetypes=(("Archivos EXCEL", "*.xlsx"), ("Todos los archivos", "*.*"))
    )
    if ruta:
        archivo_seleccionado = ruta
        nombre_base = os.path.basename(ruta)
        # Actualizamos el texto del botón para confirmar la selección
        boton_referencia.config(text=f"{nombre_base}", fg="#224222")

def ejecutar_procesamiento(entrada_texto, ventana_secundaria, etiqueta_estado):
    """Valida los datos y llama a la función de cálculo."""
    global archivo_seleccionado
    nombre_salida = entrada_texto.get().strip()
    
    if not archivo_seleccionado:
        etiqueta_estado.config(text="Error: No has seleccionado un archivo.", fg="red")
        ventana_secundaria.destroy()
        return

    if not nombre_salida:
        etiqueta_estado.config(text="Error: Debes indicar un nombre de salida.", fg="red")
        ventana_secundaria.destroy()
        return

    try:
        # Llamada a la lógica del negocio
        calculo_liquidacion(archivo_seleccionado, nombre_salida)
        etiqueta_estado.config(
            text="¡PROCESO COMPLETADO!\nRevisa tu carpeta de Descargas.", 
            fg="#224222"
        )
    except Exception as e:
        etiqueta_estado.config(text=f"Error inesperado: {e}", fg="red")
    finally:
        ventana_secundaria.destroy()

def abrir_ventana_nombre(root_ref, etiqueta_estado):
    """Crea una pequeña ventana emergente para pedir el nombre del archivo final."""
    rama2 = tk.Toplevel(root_ref) # Toplevel es mejor que un segundo tk.Tk()
    rama2.title("Nombre de salida")
    rama2.geometry("350x150") 
    rama2.config(bg="#BCE4BC")
    rama2.resizable(False, False)

    tk.Label(rama2, text="Nombre del nuevo archivo:", font=("Times New Roman", 12), bg="#BCE4BC").pack(pady=10)
    
    entrada = tk.Entry(rama2, bg="#F6F6D1", width=25, font=("Arial", 11))
    entrada.pack(pady=5)
    entrada.focus_set() # Para que el usuario pueda escribir directamente

    btn_aceptar = tk.Button(
        rama2, 
        text="Procesar Excel", 
        command=lambda: ejecutar_procesamiento(entrada, rama2, etiqueta_estado)
    )
    btn_aceptar.pack(pady=10)

def iniciar_interfaz():
    """Configuración principal de la ventana de la aplicación."""
    root = tk.Tk()  
    root.title("Liquidator v1.0")  
    root.geometry("500x400") 
    root.config(bg="#F6F6D1")
    root.resizable(False, False)

    # --- Carga de Imágenes ---
    # Nota: Asegúrate de que las imágenes estén en la carpeta 'assets'
    try:
        img_excel = Image.open(resource_path("assets/excel_logo.png")).resize((50, 50))
        logo_excel = ImageTk.PhotoImage(img_excel)
        
        img_check = Image.open(resource_path("assets/icono.png")).resize((50, 50))
        logo_check = ImageTk.PhotoImage(img_check)
    except Exception:
        # Si no encuentra las imágenes, el programa no se romperá
        logo_excel = None
        logo_check = None

    # --- Elementos Visuales ---
    tk.Label(root, text="SIMPLIFICADOR EXCEL", font=("Times New Roman", 18, "bold"), 
             bg="#F6F6D1", fg="#224222").place(x=110, y=20)

    if logo_check:
        tk.Label(root, image=logo_excel, bg="#F6F6D1").place(x=0, y=0)

    btn_seleccionar = tk.Button(
        root, 
        text="Seleccionar archivo...", 
        command=lambda: seleccionar(btn_seleccionar),
        font=("Times New Roman", 14), 
        bg="#BCE4BC",
        height=1
    )
    btn_seleccionar.place(x=150, y=160)

    # Etiqueta para mensajes de estado al usuario
    etiqueta_status = tk.Label(root, text="", font=("Arial", 11), bg="#F6F6D1", wraplength=400)
    etiqueta_status.place(x=50, y=280, width=400)

    btn_procesar = tk.Button(
        root, 
        image=logo_check, 
        command=lambda: abrir_ventana_nombre(root, etiqueta_status),
        font=("Times New Roman", 14),
        bg = "#F6F6D1",
        relief="flat",
        highlightthickness=0
    )

    btn_procesar.place(x=350, y=150)

    root.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()