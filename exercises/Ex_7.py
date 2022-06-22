## Aluno - Ricardo J Fellini
##Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário
##de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o
##usuário pode digitar letras maiúsculas ou minúsculas.

def exercicio_7():
    nome = str(input("Digite o seu nome.: ")[::-1])
    print(nome.upper())


exercicio_7()
