# Liquidator v1.0 - Simplificador Excel

**Liquidator** es una herramienta de escritorio desarrollada en Python diseñada para automatizar la consolidación de datos financieros y de liquidación. Su objetivo es simplificar el trabajo administrativo procesando múltiples hojas de cálculo para unificar registros basados en el DNI.

## Características Principales

  * **Consolidación Automática:** Lee todas las pestañas de un archivo Excel, identifica registros duplicados por DNI y suma automáticamente los valores de Base Imponible, IRPF, Seg. Social y Total.
  * **Interfaz Intuitiva:** Diseño limpio utilizando la librería `tkinter`, con selección de archivos mediante explorador nativo y ventanas emergentes de configuración.
  * **Gestión de Descargas:** El archivo resultante se guarda automáticamente en la carpeta de descargas del usuario, formateado con el estándar de decimales europeo (comas).
  * **Arquitectura Modular:** Separación clara entre la interfaz de usuario (`gui.py`) y la lógica de procesamiento de datos (`logic.py`).

## Interfaz Gráfica

La aplicación presenta un diseño minimalista con colores suaves y una navegación fluida:

| Ventana Principal | Configuración de Salida |
| :--- | :--- |
|  |  |
| Permite seleccionar el archivo origen y activar el proceso. | Solicita el nombre para el nuevo archivo consolidado. |

## Estructura del Proyecto

Basado en la organización profesional de paquetes en Python:

```text
├── main.py              # Punto de entrada de la aplicación
├── src/                 # Código fuente del paquete
│   ├── __init__.py      # Inicializador del paquete 'src'
│   ├── gui.py           # Gestión de la interfaz gráfica (Tkinter)
│   └── logic.py         # Motor de procesamiento de datos (Pandas)
├── assets/              # Recursos visuales (iconos y logos)
│   ├── excel_logo.png
│   └── icono.png
└── requirements.txt     # Dependencias del proyecto
```

## Tecnologías Utilizadas

  * **Python 3.10**: Lenguaje principal.
  * **Pandas**: Procesamiento y análisis de datos de alto rendimiento.
  * **Tkinter**: Desarrollo de la interfaz gráfica.
  * **Pillow (PIL)**: Manejo y redimensionamiento de imágenes en la interfaz.
  * **Openpyxl**: Motor para la gestión y guardado de archivos Excel.

## Funcionamiento Interno

1.  **Carga Dinámica:** El programa utiliza `resource_path` para garantizar que los iconos y logos se carguen correctamente tanto en el entorno de desarrollo como en el ejecutable final (`.exe`).
2.  **Procesamiento Eficiente:** En lugar de bucles lentos, se utiliza la función `groupby` de Pandas para agrupar y sumar miles de filas de datos de forma casi instantánea.
3.  **Detección Multiplataforma:** Localiza automáticamente la carpeta de "Downloads" o "Descargas" dependiendo del idioma del sistema operativo.

## Instalación y Uso

1.  Clona el repositorio.
2.  Instala las librerías necesarias:
    ```bash
    pip install pandas openpyxl Pillow
    ```
3.  Ejecuta la aplicación desde la raíz:
    ```bash
    python main.py
    ```

## Licencia

Este proyecto está bajo la **Licencia MIT**, lo que permite su uso y modificación libre para fines personales o profesionales.

-----

**Desarrollado por Elena**
*Simplificando procesos administrativos a través del código.*