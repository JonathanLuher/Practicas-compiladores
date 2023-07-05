import os

def verificar_sintaxis_c(codigo):
    # Contadores para verificar el equilibrio de paréntesis y llaves
    parentesis_abiertos = 0
    parentesis_cerrados = 0
    llaves_abiertas = 0
    llaves_cerradas = 0
    llav_des=False
    par_des=False
    
    # Verificar el equilibrio de paréntesis y llaves
    for caracter in codigo:
        if caracter == '(':
            parentesis_abiertos += 1
        elif caracter == ')':
            parentesis_cerrados += 1
        elif caracter == '{':
            llaves_abiertas += 1
        elif caracter == '}':
            llaves_cerradas += 1

    errores = 0
    if parentesis_abiertos != parentesis_cerrados:
        print("Error: Paréntesis desequilibrados")
        errores += 1
        par_des=True
    if llaves_abiertas != llaves_cerradas:
        print("Error: Llaves desequilibradas")
        errores += 1
        llav_des=True

    # Verificar el punto y coma al final de cada línea
    lineas = codigo.split('\n')
    for linea in lineas:
        linea = linea.strip()
        if linea and not (linea.endswith(';') or linea.endswith('{') or linea.endswith('}') or linea.endswith('>')) and par_des==False and llav_des==False:
            print(f"Error: Falta el punto y coma en la línea '{linea}'")
            errores += 1

    # Verificar la sintaxis de las funciones if
    for i, linea in enumerate(lineas):
        linea = linea.strip()
        if linea.startswith('if'):
            if '(' not in linea or ')' not in linea:
                print(f"Error: Sintaxis incorrecta en la línea {i + 1}, se esperaba '(' y ')'")
                if par_des==True:
                    errores = errores
                else:
                    errores +=1
            elif '{' not in linea:
                for j in range(i + 1, len(lineas)):
                    if '{' in lineas[j]:
                        break
                else:
                    print(f"Error: Sintaxis incorrecta en la línea {i + 1}, falta abrir llaves '{{'")
                    if par_des==True:
                        errores = errores
                    else:
                        errores +=1

    if errores == 0:
        print("Sin errores de sintaxis")
    else:
        print("Número de errores encontrados:", errores)

# Obtener la ruta absoluta del archivo .c basado en la ruta del programa
ruta_programa = os.path.abspath(__file__)
ruta_c = os.path.join(os.path.dirname(ruta_programa), "codigo.c")

try:
    with open(ruta_c, 'r') as file:
        codigo_c = file.read()
        verificar_sintaxis_c(codigo_c)
except FileNotFoundError:
    print("El archivo no se encontró.")
except IOError:
    print("Error al leer el archivo.")
