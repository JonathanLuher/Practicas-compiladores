import os
from PIL import Image

def convertir_a_binario(imagen):
    imagen_bn = imagen.convert('L')  # Convertir la imagen a blanco y negro
    ancho, alto = imagen_bn.size
    matriz_binaria = []

    for y in range(alto):
        fila = []
        for x in range(ancho):
            pixel = imagen_bn.getpixel((x, y))
            if pixel < 128:  # Si el pixel es oscuro
                fila.append(1)
            else:  # Si el pixel es claro
                fila.append(0)
        matriz_binaria.append(fila)

    return matriz_binaria

def guardar_matrices(matrices, archivo):
    with open(archivo, 'w') as f:
        for matriz in matrices:
            fila_str = ' '.join(map(str, matriz))  # Convertir la fila a cadena de texto
            f.write(fila_str + '\n')
        f.write('\n')

# Carpeta que contiene las imágenes de entrada
carpeta_imagenes = 'imagenes'

# Crear una carpeta para los archivos de salida
carpeta_salida = 'matrices'
os.makedirs(carpeta_salida, exist_ok=True)

# Recorrer todas las imágenes en la carpeta
for nombre_imagen in os.listdir(carpeta_imagenes):
    ruta_imagen = os.path.join(carpeta_imagenes, nombre_imagen)
    if os.path.isfile(ruta_imagen):
        # Abrir la imagen y convertirla a matriz binaria
        imagen = Image.open(ruta_imagen)
        matriz_binaria = convertir_a_binario(imagen)

        # Generar el nombre del archivo de salida
        nombre_archivo = os.path.splitext(nombre_imagen)[0] + '.txt'
        ruta_archivo = os.path.join(carpeta_salida, nombre_archivo)

        # Guardar la matriz en el archivo de texto correspondiente
        guardar_matrices(matriz_binaria, ruta_archivo)

print('Se han generado los archivos de texto en la carpeta', carpeta_salida)
