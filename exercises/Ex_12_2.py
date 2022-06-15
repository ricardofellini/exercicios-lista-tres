matrizA = [[0, 0], [0, 0]]
matrizB = [[0, 0], [0, 0]]
matrizC = [[0, 0], [0, 0]]


def recebeMatriz():
    for i in range(0, 2):
        for j in range(0, 2):
            matrizA[i][j] = int(input(f"Digite os valores da Matriz A:"))

    for i in range(0, 2):
        for j in range(0, 2):
            matrizB[i][j] = int(input(f"Digite os valores da Matriz B.:"))


def multiplicaMatrizes():
    numeroLinhasA, numeroLinhasB = len(matrizA), len(matrizB)
    numeroColunasA, numeroColunasB = len(matrizA[0]), len(matrizB[0])

    if (numeroLinhasA == numeroLinhasB) and (numeroColunasA == numeroColunasB):
        for i in range(numeroLinhasA):
            for j in range(numeroColunasA):
                matrizC[i][j] = matrizA[i][j] * matrizB[i][j]
    else:
        print("Não é possível multiplicar matrizes com colunas/linhas diferentes! ")

    print("Matriz A.:", matrizA)
    print("Matriz B.:", matrizB)
    print("Matriz C.:", matrizC)


recebeMatriz()
multiplicaMatrizes()
