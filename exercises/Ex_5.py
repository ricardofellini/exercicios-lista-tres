## Aluno - Ricardo J Fellini
##Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
##elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 98]
lista2 = [21, 32, 43, 54, 65, 76, 98, 34, 44, 55]
lista3 = []


def exercicio_5():
    for i in range(0, len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    print(lista3)


exercicio_5()
