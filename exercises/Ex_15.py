## Aluno - Ricardo J Fellini


##Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de
##caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def exercicio_15(a):

    if a <= 0:
        return "N"
    elif a > 0:
        return "P"


print(exercicio_15(-3))
