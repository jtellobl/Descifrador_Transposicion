import math 


def descifrar_transposicion(cifrado, clave): 

    num_columnas = len(clave) 

    num_filas = math.ceil(len(cifrado) / num_columnas) 

     

    matriz = [''] * num_columnas 

    col_largo = len(cifrado) // num_columnas 

     

    # Llenar columnas de acuerdo a la clave 

    indice = 0 

    for i in clave: 

        matriz[int(i) - 1] = cifrado[indice:indice + col_largo] 

        indice += col_largo 

     

    # Leer los caracteres en orden de filas 

    descifrado = '' 

    for fila in range(num_filas): 

        for columna in range(num_columnas): 

            if fila < len(matriz[columna]): 

                descifrado += matriz[columna][fila] 

     

    return descifrado.strip() 

  

if __name__ == "__main__": 

    # Solicitar texto cifrado y clave 

    texto_cifrado = input("Introduce el texto cifrado: ") 

    clave = input("Introduce la clave (números sin espacios): ") 

     

    # Descifrar el texto 

    texto_descifrado = descifrar_transposicion(texto_cifrado, clave) 

    print(f'Texto descifrado: {texto_descifrado}') 

 
