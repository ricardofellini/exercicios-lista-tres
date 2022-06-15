numero = int(input("Digite o número escolhido.:"))


def linha(numero):
    for i in range(1, numero + 1):
        print(f" {i} ", end='')
    print()


def sequencia(numero):
    for numero in range(numero + 1):
        linha(numero)


sequencia(numero)
