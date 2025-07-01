"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


# pylint: disable=import-outside-toplevel

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    # Leer el archivo CSV
    df = pd.read_csv("files/input/news.csv")

    # Crear gráfico
    plt.figure(figsize=(10, 6))

    # Trazar cada medio (columnas excepto la primera que es el año)
    for columna in df.columns[1:]:
        plt.plot(df["Unnamed: 0"], df[columna], marker="o", label=columna)

    # Configurar gráfico
    plt.title("Tendencias de medios de noticias (2001–2010)")
    plt.xlabel("Año")
    plt.ylabel("Porcentaje (%)")
    plt.legend()
    plt.grid(True)

    # Asegurar carpeta de salida
    os.makedirs("files/plots", exist_ok=True)

    # Guardar imagen
    plt.savefig("files/plots/news.png")
    plt.close()
