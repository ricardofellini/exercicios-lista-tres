## Aluno - Ricardo J Fellini
##Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe
##também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

def exercicio_6():
    listaStrings = []

    for i in range(0, 2):
        string = (str(input(f"Digite o valor da {i + 1} String.:\n")))
        listaStrings.append(string)

    for j in range(len(listaStrings)):
        print(f"{j + 1} String digitada.: ", listaStrings[j])

    for k in range(len(listaStrings)):
        print(f"Tamanho de {listaStrings[k]} é.: ", len(listaStrings[k]), " caracteres")


exercicio_6()
