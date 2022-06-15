numeros = [2, 3, 4, 12, 32, 4, 11, 22, 45, 5]


def exercicio_4():
    somaQuadrados = 0
    for i in range(0, len(numeros)):
        somaQuadrados = somaQuadrados + numeros[i] ** 2
    print("Números da lista.: ", numeros)
    print("A soma dos números elevados ao quadrado é.: ", somaQuadrados)


exercicio_4()
