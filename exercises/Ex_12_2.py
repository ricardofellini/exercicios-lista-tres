## Aluno - Ricardo J Fellini

##Faça um programa que leia as dimensões de duas matrizes A e B, e depois leia as duas matrizes (os
##elementos devem ser inteiros). Se as matrizes forem de tamanhos compatíveis para multiplicação,
## multiplique as matrizes. Imprima as matrizes A, B e a matriz resultante da multiplicação.
matrizA = [[0, 0],
           [0, 0]]
matrizB = [[0, 0], [0, 0]]
matrizC = [[0, 0],
           [0, 0]]


def recebeMatriz():
    for i in range(0, 2):
        for j in range(0, 2):
            matrizA[i][j] = int(input(f"Digite os valores da Matriz A:"))

    for i in range(0, 2):
        for j in range(0, 2):
            matrizB[i][j] = int(input(f"Digite os valores da Matriz B.:"))


def multiplicaMatrizes():
    numeroLinhasA = len(matrizA[0])
    numeroLinhasB = len(matrizB[0])

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
