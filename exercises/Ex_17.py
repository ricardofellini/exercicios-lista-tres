## Aluno - Ricardo J Fellini

##Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve
##receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e
##o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para
##valores dentro da faixa de forma elegante.

qtdeLinha = int(input("Qtde de +-----+ .:"))
qtdeColuna = int(input("Digite a quantidade de |   | .:"))


def validacaoValorDosDados(valor):

    if valor < 1 or valor > 20:
        return 20
    else:
        return valor

def fazerLinha(qtdeLinha):
    caracter = "+"
    for i in range(qtdeLinha):
        caracter += "-"
    caracter += "+"
    print(caracter)


def fazerColuna(qtdeLinha, qtdeColuna):
    for i in range(qtdeColuna):
        caracter = "|"
        caracter += " " * qtdeLinha
        caracter += "|"
        print(caracter)

def desenhaRetangulo(qtdeLinha, qtdeColuna):
    fazerLinha(qtdeLinha)
    fazerColuna(qtdeLinha, qtdeColuna)
    fazerLinha(qtdeLinha)


desenhaRetangulo(validacaoValorDosDados(qtdeLinha), validacaoValorDosDados(qtdeColuna))
