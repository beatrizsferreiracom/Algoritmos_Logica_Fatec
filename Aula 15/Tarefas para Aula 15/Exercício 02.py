#2) Altere o programa para trabalhar com 2 vetores. Além do vetor de cidade, adicione o vetor de população:

cidades = []
populacoes = []

for i in range(5):
    cidade = input(f"Digite o nome da cidade {i+1}: ")
    populacao = int(input(f"Digite a população da cidade {i+1}: "))
    cidades.append(cidade)
    populacoes.append(populacao)

# Combinar as cidades e populações em uma lista de tuplas e ordenar
cidades_populacoes = list(zip(cidades, populacoes))
cidades_populacoes.sort()

print("Cidades em ordem alfabética com suas populações:")
for cidade, populacao in cidades_populacoes:
    print(f"{cidade}: {populacao}")
