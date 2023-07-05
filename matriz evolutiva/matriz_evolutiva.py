import random

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    return contenido

def obtener_palabras(texto):
    # Eliminar caracteres especiales y convertir a minúsculas
    texto = ''.join(c for c in texto if c.isalnum() or c.isspace())
    texto = texto.lower()

    palabras = texto.split()
    return palabras

def generar_matriz(palabras):
    tamano = len(palabras)
    matriz = [[0] * tamano for _ in range(tamano)]
    return matriz

def actualizar_matriz(palabras, matriz):
    tamano = len(palabras)
    for i in range(tamano-1):
        palabra_actual = palabras[i]
        palabra_siguiente = palabras[i+1]
        indice_actual = palabras.index(palabra_actual)
        indice_siguiente = palabras.index(palabra_siguiente)
        matriz[indice_actual][indice_siguiente] += 1
    return matriz

def escribir_palabras(palabras, nombre_archivo):
    palabras_existentes = set()
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        palabras_existentes = set(archivo.read().splitlines())

    with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
        for palabra in palabras:
            if palabra not in palabras_existentes:
                archivo.write(palabra + '\n')
                palabras_existentes.add(palabra)

def calcular_probabilidades(matriz, suavizado=1):
    matriz_probabilidades = []
    for fila in matriz:
        total = sum(fila) + suavizado * len(fila)
        fila_probabilidades = [(valor + suavizado) / total for valor in fila]
        matriz_probabilidades.append(fila_probabilidades)
    return matriz_probabilidades

def generar_texto(matriz_probabilidades, palabras, longitud):
    texto_generado = [random.choice(palabras)]
    while len(texto_generado) < longitud:
        ultima_palabra = texto_generado[-1]
        indice_ultima_palabra = palabras.index(ultima_palabra)
        probabilidad_fila = matriz_probabilidades[indice_ultima_palabra]
        siguiente_palabra = random.choices(palabras, weights=probabilidad_fila, k=1)[0]
        texto_generado.append(siguiente_palabra)
    return ' '.join(texto_generado)

def guardar_matriz(matriz, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        for fila in matriz:
            archivo.write(','.join(str(valor) for valor in fila))
            archivo.write('\n')

def guardar_texto(texto, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)

archivo_texto = 'texto.txt'
archivo_palabras = 'lista_palabras.txt'
archivo_matriz = 'matriz.txt'
archivo_probabilidades = 'matriz_probabilidades.txt'
archivo_texto_generado = 'texto_generado.txt'

contenido_texto = leer_archivo(archivo_texto)
palabras_encontradas = obtener_palabras(contenido_texto)

matriz_ceros = generar_matriz(palabras_encontradas)
matriz_actualizada = actualizar_matriz(palabras_encontradas, matriz_ceros)
matriz_probabilidades = calcular_probabilidades(matriz_actualizada, suavizado=1)

escribir_palabras(palabras_encontradas, archivo_palabras)
guardar_matriz(matriz_actualizada, archivo_matriz)
guardar_matriz(matriz_probabilidades, archivo_probabilidades)

print(f'Se han encontrado {len(palabras_encontradas)} palabras y se han guardado en {archivo_palabras}.')
print(f'Se ha generado una matriz de ceros del tamaño {len(palabras_encontradas)}x{len(palabras_encontradas)}.')
print(f'Se ha guardado la matriz de frecuencias en {archivo_matriz}.')
print(f'Se ha guardado la matriz de probabilidades en {archivo_probabilidades}.')

longitud_texto_generado = 100  # Longitud del texto generado
texto_generado = generar_texto(matriz_probabilidades, palabras_encontradas, longitud_texto_generado)
guardar_texto(texto_generado, archivo_texto_generado)

print(f'Se ha generado el texto en {archivo_texto_generado}.')
