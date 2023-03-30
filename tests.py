import numpy as np

matriz = np.array([[165, 0, 0, 0, 0, 0],
                   [35, 0, 0, 0, 0, 0],
                   [180, 0, 0, 0, 0, 0],
                   [50, 0, 0, 0, 0, 0],
                   [35, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0]])

filas = len(matriz)
columnas = len(matriz[0])

for i in range(filas):
    for j in range(columnas - 1):
        if matriz[i][j] >= 1 and matriz[i][j+1] >= 1 and matriz[i][j] == matriz[i][j+1]:
            print(f"El número {matriz[i][j]} en la fila {i} y columna {j} tiene un vecino igual a su derecha.")



print(matriz)