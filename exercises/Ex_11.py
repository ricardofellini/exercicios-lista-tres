## Aluno - Ricardo J Fellini
##Faça um programa que leia duas matrizes A e B 2x2 de inteiros e imprima a matriz C que é a soma
##das matrizes A e B.

def exercicio_11():
    matrizA = [[1, 2], [5, 5]]
    matrizB = [[3, 4], [7, 8]]
    matrizC = []

    for i in range(len(matrizA)):
        matrizC.append([])
        for j in range(len(matrizA)):
            matrizC[i].append(matrizA[i][j] + matrizB[i][j])
        print(matrizC[i])

exercicio_11()
