## Aluno - Ricardo J Fellini
##Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

def exercicio_8():
    nome = str(input("Digite o nome.:"))

    for letras in range(len(nome)):
        print(nome[letras])


exercicio_8()
