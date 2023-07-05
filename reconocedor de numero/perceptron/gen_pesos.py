import os
import numpy as np

def cargar_matrices_desde_archivos(carpeta):
    matrices = []
    archivos = os.listdir(carpeta)

    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        if archivo.endswith(".txt"):
            with open(ruta_archivo, "r") as archivo_matriz:
                contenido = archivo_matriz.read()
                contenido = contenido.strip().split("\n")
                matriz = []
                for fila in contenido:
                    try:
                        fila = fila.strip().split()
                        fila = [int(valor) for valor in fila]
                        matriz.append(fila)
                    except ValueError:
                        continue  # Ignorar filas no válidas
                if matriz:
                    matrices.append(matriz)

    return matrices

def calcular_peso_total(matrices):
    peso_total = np.zeros_like(matrices[0], dtype=int)

    for matriz in matrices:
        peso_total += matriz

    return peso_total

def generar_archivos_de_texto(carpeta):
    if not os.path.exists(carpeta):
        print("La carpeta no existe.")
        return

    carpetas = os.listdir(carpeta)

    for subcarpeta in carpetas:
        ruta_subcarpeta = os.path.join(carpeta, subcarpeta)
        if os.path.isdir(ruta_subcarpeta):
            matrices = cargar_matrices_desde_archivos(ruta_subcarpeta)
            peso_total = calcular_peso_total(matrices)

            # Crear carpeta "pesos" si no existe
            carpeta_pesos = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pesos")
            if not os.path.exists(carpeta_pesos):
                os.makedirs(carpeta_pesos)

            archivo_salida = os.path.join(carpeta_pesos, subcarpeta + ".txt")
            with open(archivo_salida, "w") as archivo:
                for fila in peso_total:
                    archivo.write(" ".join(map(str, fila)) + "\n")

            print("Se ha generado el archivo de salida para la carpeta:", subcarpeta)

# Ruta de la carpeta con subcarpetas
carpeta_path = "matrices"

# Generar archivos de texto para cada subcarpeta dentro de la carpeta
generar_archivos_de_texto(carpeta_path)
