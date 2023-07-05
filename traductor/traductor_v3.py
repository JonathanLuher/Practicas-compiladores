import tkinter as tk
from tkinter import messagebox

traducciones = []
traducciones2 = []

entrada_palabra = None
ventana_agregar = None

def cargar_traducciones():
    try:
        with open("archivo_traducciones.txt", "r") as archivo:
            for linea in archivo:
                traducciones.append(linea.strip())
    except FileNotFoundError:
        messagebox.showwarning("Error", "No se encontró el archivo 'archivo_traducciones.txt'.")

    try:
        with open("archivo_traducciones2.txt", "r") as archivo:
            for linea in archivo:
                traducciones2.append(linea.strip())
    except FileNotFoundError:
        messagebox.showwarning("Error", "No se encontró el archivo 'archivo_traducciones2.txt'.")

def guardar_traducciones():
    with open("archivo_traducciones.txt", "w") as archivo:
        for palabra in traducciones:
            archivo.write(palabra + "\n")

    with open("archivo_traducciones2.txt", "w") as archivo:
        for palabra in traducciones2:
            archivo.write(palabra + "\n")

def mostrar_tabla():
    tabla = "---TABLA DE TRADUCCIONES---\n"
    for palabra_s, palabra_e in zip(traducciones2, traducciones):
        tabla += palabra_s + " - " + palabra_e + "\n"
    messagebox.showinfo("Tabla de Traducciones", tabla)

def calcular_similitud_jaccard(palabra1, palabra2):
    set1 = set(palabra1)
    set2 = set(palabra2)
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    similitud = intersection / union
    return similitud

def corregir_palabra(palabra):
    mejor_correccion = None
    mejor_similitud = 0

    for palabra_traducida in traducciones + traducciones2:
        similitud = calcular_similitud_jaccard(palabra, palabra_traducida)
        if similitud > mejor_similitud:
            mejor_similitud = similitud
            mejor_correccion = palabra_traducida

    return mejor_correccion

def agregar_palabra(palabra, idioma):
    global ventana_agregar
    ventana_agregar.destroy()

    ventana_traduccion = tk.Toplevel()
    ventana_traduccion.title("Agregar Traducción")

    etiqueta_traduccion = tk.Label(ventana_traduccion, text="Introduzca la traducción:")
    etiqueta_traduccion.pack()

    entrada_traduccion = tk.Entry(ventana_traduccion)
    entrada_traduccion.pack()

    def agregar():
        traduccion = entrada_traduccion.get()
        if idioma == "español":
            traducciones2.append(palabra)
            traducciones.append(traduccion)
        elif idioma == "ingles":
            traducciones.append(palabra)
            traducciones2.append(traduccion)

        messagebox.showinfo("Éxito", "Palabra agregada con éxito.")
        ventana_traduccion.destroy()
        mostrar_tabla()

    boton_agregar = tk.Button(ventana_traduccion, text="Agregar", command=agregar)
    boton_agregar.pack()

def traducir_palabra():
    global ventana_agregar
    palabra = entrada_palabra.get().lower()

    for palabra_s, palabra_e in zip(traducciones2, traducciones):
        if palabra == palabra_s.lower():
            traduccion_encontrada = True
            messagebox.showinfo("Traducción", "La traducción de la palabra es: " + palabra_e)
            break
        elif palabra == palabra_e.lower():
            traduccion_encontrada = True
            messagebox.showinfo("Traducción", "La traducción de la palabra es: " + palabra_s)
            break
    else:
        correccion = corregir_palabra(palabra)

        if correccion is not None:
            similitud = calcular_similitud_jaccard(palabra, correccion)
            if similitud > 0.6:
                ventana_error = tk.Toplevel()
                ventana_error.title("Error")
                ventana_error.geometry("300x150")

                etiqueta_error = tk.Label(ventana_error, text="Palabra incorrecta:")
                etiqueta_error.pack()

                etiqueta_error_palabra = tk.Label(ventana_error, text=palabra)
                etiqueta_error_palabra.pack()

                etiqueta_correccion = tk.Label(ventana_error, text="Corrección sugerida:")
                etiqueta_correccion.pack()

                etiqueta_correccion_palabra = tk.Label(ventana_error, text=correccion)
                etiqueta_correccion_palabra.pack()

                for palabra_traducida, palabra_traducida2 in zip(traducciones, traducciones2):
                    if correccion == palabra_traducida:
                        etiqueta_traduccion = tk.Label(ventana_error, text="Traducción sugerida:")
                        etiqueta_traduccion.pack()

                        etiqueta_traduccion_palabra = tk.Label(ventana_error, text=palabra_traducida2)
                        etiqueta_traduccion_palabra.pack()
                        break
                    elif correccion == palabra_traducida2:
                        etiqueta_traduccion = tk.Label(ventana_error, text="Traducción sugerida:")
                        etiqueta_traduccion.pack()

                        etiqueta_traduccion_palabra = tk.Label(ventana_error, text=palabra_traducida)
                        etiqueta_traduccion_palabra.pack()
                        break
            else:
                ventana_agregar = tk.Toplevel()
                ventana_agregar.title("Agregar Traducción")

                etiqueta_idioma = tk.Label(ventana_agregar, text="Seleccione el idioma de la palabra:")
                etiqueta_idioma.pack()

                boton_espanol = tk.Button(ventana_agregar, text="Español", command=lambda: agregar_palabra(palabra, "español"))
                boton_espanol.pack()

                boton_ingles = tk.Button(ventana_agregar, text="Inglés", command=lambda: agregar_palabra(palabra, "ingles"))
                boton_ingles.pack()

        else:
            messagebox.showwarning("Palabra no encontrada", "La palabra no se encuentra en el diccionario.")

def iniciar_programa():
    global entrada_palabra

    ventana_inicio.destroy()

    cargar_traducciones()

    ventana = tk.Tk()
    ventana.title("Traductor")
    ventana.geometry("300x200")

    etiqueta_palabra = tk.Label(ventana, text="Introduzca la palabra que desea traducir:")
    etiqueta_palabra.pack()

    entrada_palabra = tk.Entry(ventana)
    entrada_palabra.pack()

    boton_traducir = tk.Button(ventana, text="Traducir", command=traducir_palabra)
    boton_traducir.pack()

    boton_mostrar_tabla = tk.Button(ventana, text="Mostrar Tabla", command=mostrar_tabla)
    boton_mostrar_tabla.pack()

    ventana.protocol("WM_DELETE_WINDOW", lambda: on_closing(ventana))
    ventana.mainloop()

def on_closing(ventana):
    guardar_traducciones()
    ventana.destroy()

ventana_inicio = tk.Tk()
ventana_inicio.title("Bienvenido")
ventana_inicio.geometry("300x150")

etiqueta_inicio = tk.Label(ventana_inicio, text="¿Qué desea hacer?")
etiqueta_inicio.pack()

boton_iniciar_programa = tk.Button(ventana_inicio, text="Iniciar programa", command=iniciar_programa)
boton_iniciar_programa.pack()

boton_salir = tk.Button(ventana_inicio, text="Salir", command=ventana_inicio.quit)
boton_salir.pack()

ventana_inicio.mainloop()
