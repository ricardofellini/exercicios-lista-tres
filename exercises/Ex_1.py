## Aluno - Ricardo J Fellini
##Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de
## cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []


def exercicio_1():
    alunosAcimaMedia = 0

    for aluno in range(10):
        totalNotas = 0
        for nota in range(4):
            print("Digite a ", nota + 1, "nota do ", aluno + 1, "aluno")
            totalNotas += float(input())
        medias.append(totalNotas / 4)

        if medias[aluno] >= 7.0:
            alunosAcimaMedia += 1

    print("Médias.:", medias)
    print("Número de alunos com média maior que 7.:", alunosAcimaMedia)

exercicio_1()
