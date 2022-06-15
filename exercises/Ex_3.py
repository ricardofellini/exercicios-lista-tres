idades = []
alturas = []


def exercicio_3():
    for i in range(0, 5):
        idades.append(int(input(f"Digite a idade.: {i+1}\n")))
        alturas.append(float(input(f"Digite a altura.: {i+1}\n")))

    print("Alturas.:")
    print(alturas[::-1])

    print("Idades.:")
    print(idades[::-1])


exercicio_3()
