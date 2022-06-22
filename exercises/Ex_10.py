## Aluno - Ricardo J Fellini
##Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal principal
##da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação.

matriz = [[3, 4, 5],
          [6, 7, 8],
          [9, 7, 6]]


def exercicio_10():
    print("Matriz antes da manipulação.:")
    for i in range(len(matriz)):
        print(matriz[i])

    print("Matriz após da manipulação.:")
    for j in range(len(matriz)):
        matriz[j][j] = matriz[j][j] * 4

        print(matriz[j])


exercicio_10()
