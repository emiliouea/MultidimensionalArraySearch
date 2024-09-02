def buscar_valor_matriz(matriz, valor_buscado):
    """
    Busca un valor en una matriz bidimensional y devuelve su posición si se encuentra.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Devuelve la posición (fila, columna)
    return None  # Valor no encontrado

# Matriz de ejemplo
matriz = [
    [5, 3, 9],
    [1, 7, 2],
    [6, 8, 4]
]

# Valor a buscar
valor = 7

# Buscar el valor en la matriz
resultado = buscar_valor_matriz(matriz, valor)

# Mostrar resultados
if resultado:
    print(f"Valor {valor} encontrado en la posición: {resultado}")
else:
    print(f"Valor {valor} no encontrado en la matriz.")
