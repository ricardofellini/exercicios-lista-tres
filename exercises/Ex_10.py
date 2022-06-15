matriz = [[3, 4, 5],
          [6, 7, 8], [9, 7, 6]]


def exercicio_10():
    print("Matriz antes da manipulação.:")
    for i in range(len(matriz)):
        print(matriz[i])

    print("Matriz após da manipulação.:")
    for j in range(len(matriz)):
        matriz[j][j] = matriz[j][j] * 4

        print(matriz[j])


exercicio_10()
