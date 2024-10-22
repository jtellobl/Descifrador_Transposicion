import math

def descifrar_transposicion_simple(cifrado):
    # Definir el número de columnas (fijo en 4)
    num_columnas = 4
    num_filas = math.ceil(len(cifrado) / num_columnas)
    
    # Crear una lista para los caracteres de cada columna
    matriz = [''] * num_filas
    
    # Calcular el número de caracteres en cada columna
    col_largo_base = len(cifrado) // num_columnas
    col_largo_extra = len(cifrado) % num_columnas
    
    # Llenar la matriz con los caracteres en orden de columnas
    indice = 0
    for columna in range(num_columnas):
        largo_columna = col_largo_base + 1 if columna < col_largo_extra else col_largo_base
        for fila in range(largo_columna):
            if indice < len(cifrado):
                if len(matriz[fila]) < num_columnas:
                    matriz[fila] += cifrado[indice]
                indice += 1
    
    # Concatenar los caracteres para formar el texto descifrado
    descifrado = ''.join(matriz).strip()
    return descifrado

if __name__ == "__main__":
    # Solicitar el texto cifrado
    texto_cifrado = input("Introduce el texto cifrado: ")
    
    # Descifrar el texto
    texto_descifrado = descifrar_transposicion_simple(texto_cifrado)
    print(f'Texto descifrado: {texto_descifrado}')
