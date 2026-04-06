from src.gui import iniciar_interfaz

def main():
    """
    Punto de entrada principal de la aplicación.
    Lanza la interfaz gráfica definida en el paquete src.
    """
    try:
        iniciar_interfaz()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    main()