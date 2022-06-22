## Aluno - Ricardo J Fellini
##Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato
##de escada.

def exercicio_9():
    nome = str(input("Digite o nome.:"))
    nome2 = ""

    for i in range(len(nome)):
        nome2 = nome2 + nome[i]
        print(nome2)

exercicio_9()

