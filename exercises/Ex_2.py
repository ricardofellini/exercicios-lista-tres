## Aluno - Ricardo J Fellini
##Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os
##números.


from math import prod

def exercicio_2():
    numeros = []

    for i in range(0, 5):
        numeros.append(int(input(f"Digite valor.: {i+1}\n")))
    soma = sum(numeros)
    multiplicacao = prod(numeros)

    print("A soma dos valores digitados é.:", soma)
    print("A multiplicação dos valores digitados é.:", multiplicacao)
    print("Os valores digitados foram.:", numeros)

exercicio_2()
