"""
Excel Simplificador Package
---------------------------
Este paquete contiene la lógica de procesamiento de datos y la 
interfaz gráfica para la consolidación de archivos Excel.
"""

# Importamos las funciones principales para que estén disponibles 
# directamente desde el paquete 'src'
from .logic import calculo_liquidacion, resource_path
from .gui import seleccionar, abrir_ventana_nombre

# Esto define qué se exporta cuando alguien hace: from src import *
__all__ = [
    'calculo_liquidacion',
    'resource_path',
    'seleccionar',
    'seleccionar_nombre'
]

__version__ = '1.0.0'
__author__ = 'Elena'