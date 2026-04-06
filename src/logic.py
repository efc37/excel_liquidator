import pandas as pd
import os
import sys

def resource_path(relative_path):
    """
    Gestiona las rutas de archivos para que funcionen tanto en desarrollo 
    como cuando el programa se convierte en un ejecutable (.exe).
    """
    try:
        # PyInstaller crea una carpeta temporal y guarda la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def obtener_ruta_descargas():
    """
    Detecta la carpeta de descargas del usuario de forma multiplataforma.
    """
    home = os.path.expanduser("~")
    descargas = os.path.join(home, "Downloads")
    if not os.path.exists(descargas):
        descargas = os.path.join(home, "Descargas")
    return descargas

def guardar_excel_profesional(df, nombre_archivo):
    """
    Formatea el DataFrame para que los decimales usen comas (estándar español)
    y lo guarda en la carpeta de descargas.
    """
    ruta_descargas = obtener_ruta_descargas()
    ruta_final = os.path.join(ruta_descargas, f"{nombre_archivo}.xlsx")

    # Redondeamos a 2 decimales y cambiamos el punto por la coma para Excel
    df_formateado = df.copy()
    
    # Aplicar formato solo a columnas numéricas (float)
    cols_float = df_formateado.select_dtypes(include=['float']).columns
    for col in cols_float:
        df_formateado[col] = df_formateado[col].map(
            lambda x: str(round(x, 2)).replace('.', ',') if pd.notnull(x) else x
        )

    # Guardar usando openpyxl
    df_formateado.to_excel(ruta_final, index=False, engine='openpyxl')
    return ruta_final

def calculo_liquidacion(archivo_path, nombre_salida):
    """
    Lee todas las pestañas de un Excel, identifica personas por DNI y
    suma sus valores de Base Imponible, IRPF, Seg. Social y Total.
    """
    # 1. Cargar todas las pestañas del archivo
    # Usamos sheet_name=None para obtener un diccionario de DataFrames
    dict_hojas = pd.read_excel(archivo_path, decimal=',', sheet_name=None)
    
    # 2. Concatenar todas las hojas en una sola tabla
    df_total = pd.concat(dict_hojas.values(), ignore_index=True)
    
    # 3. Identificar columnas (DNI suele ser la primera)
    columnas = list(df_total.columns)
    col_dni = columnas[0]
    
    # Columnas a sumar
    cols_a_sumar = columnas[3:]

    # 4. Agrupar y Sumar (Forma eficiente con Pandas)
    # En lugar de un bucle 'for', usamos 'groupby' que es mucho más rápido
    solucion = df_total.groupby(col_dni, as_index=False).agg({
        **{col: 'first' for col in columnas[1:3]}, # Mantiene Nombre/Apellidos
        **{col: 'sum' for col in cols_a_sumar}     # Suma los valores numéricos
    })

    # 5. Guardar el resultado
    guardar_excel_profesional(solucion, nombre_salida)