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
