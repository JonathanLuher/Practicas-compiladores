import os

def funcion():
    def leer_matriz(nombre_archivo):
        matriz = []
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                fila = [int(elemento) for elemento in linea.split()]
                matriz.append(fila)
        return matriz

    def comparar_matrices(matriz1, matriz2):
        if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
            return 0

        coincidencias = 0
        for i in range(len(matriz1)):
            for j in range(len(matriz1[0])):
                if matriz1[i][j] == matriz2[i][j]:
                    coincidencias += 1
        return coincidencias

    # Leer la matriz de entrada
    matriz1 = leer_matriz('matriz_entrada/matriz_in.txt')

    # Obtener la lista de archivos de texto en la carpeta "numeros"
    carpeta = 'numeros'
    archivos = [nombre_archivo for nombre_archivo in os.listdir(carpeta) if nombre_archivo.endswith('.txt')]

    # Leer las matrices de comparación
    matrices = []
    for nombre_archivo in archivos:
        matriz = leer_matriz(os.path.join(carpeta, nombre_archivo))
        matrices.append(matriz)

    # Verificar la cantidad de elementos coincidentes con cada matriz
    coincidencias = []
    for i, matriz in enumerate(matrices):
        cantidad_coincidencias = comparar_matrices(matriz1, matriz)
        coincidencias.append(cantidad_coincidencias)
        print("Coincidencias con el archivo", archivos[i], ":", cantidad_coincidencias)

    # Encontrar la matriz con mayor cantidad de coincidencias
    max_coincidencias = max(coincidencias)
    if max_coincidencias > 340:
        numero_reconocido = coincidencias.index(max_coincidencias)
        print("El número fue reconocido como un:", numero_reconocido)
    else:
        print("El número no fue reconocido.")

init = int(input("---BIENVENIDO---\n1.-Iniciar programa.\n2.-Salir\nEliga su opción: "))
while init == 1:
    funcion()
    init = int(input("1.-Iniciar nuevamente el programa.\n2.-Salir\nEliga su opción: "))
