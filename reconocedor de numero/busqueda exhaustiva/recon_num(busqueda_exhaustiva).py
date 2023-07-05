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
            return False

        for i in range(len(matriz1)):
            for j in range(len(matriz1[0])):
                if matriz1[i][j] != matriz2[i][j]:
                    return False
        return True

    # Leer las matrices desde los archivos
    matriz1 = leer_matriz('numeros/matriz_in.txt')
    matriz2 = leer_matriz('numeros/cero.txt')
    matriz3 = leer_matriz('numeros/uno.txt')
    matriz4 = leer_matriz('numeros/dos.txt')
    matriz5 = leer_matriz('numeros/tres.txt')
    matriz6 = leer_matriz('numeros/cuatro.txt')
    matriz7 = leer_matriz('numeros/cinco.txt')
    matriz8 = leer_matriz('numeros/seis.txt')
    matriz9 = leer_matriz('numeros/siete.txt')
    matriz10 = leer_matriz('numeros/ocho.txt')
    matriz11 = leer_matriz('numeros/nueve.txt')

    matrices = [matriz2,matriz3,matriz4,matriz4,matriz5,matriz6,matriz8,matriz9,matriz10,matriz11]

    # Verificar si las matrices son iguales
    i=-1
    for k in (matrices):
        i=i+1
        if comparar_matrices(matriz1, k):
            print("El numero fue reconocido como un:",i)
            break
        elif(i==9):
            i=i+1
            break
    if(i==10):
        print("El numero no fue reconocido.")

init=int(input("---BIENVENIDO---\n1.-Iniciar programa.\n2.-Salir\nEliga su opcion: "))
while init==1:
        funcion()
        init=int(input("1.-Iniciar nuevamente el programa.\n2.-Salir\nEliga su opcion: "))