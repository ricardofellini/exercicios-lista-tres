def somaImposto(taxaImposto, custo):
    custoAposTaxa = custo + (custo * taxaImposto / 100)
    return f"O valor do custo após o imposto é.: ", custoAposTaxa


print(somaImposto(10, 30))
