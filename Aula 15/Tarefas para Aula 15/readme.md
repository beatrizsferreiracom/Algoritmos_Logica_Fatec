### EXERCÍCIOS DO DIA 17/05/2024

## Exercício 1

- Teste o programa:

````
idades = []

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)

idade_mais_alta = max(idades)
idade_mais_baixa = min(idades)

print(f"A idade mais alta é: {idade_mais_alta}")
print(f"A idade mais baixa é: {idade_mais_baixa}")
````

- Altere o programa para trabalhar com o vetor de nomes de alunos junto com o vetor de notas de alunos.

<hr>

## Exercício 2

- Teste o programa:

````
cidades = []

for i in range(5):
    cidade = input(f"Digite o nome da cidade {i+1}: ")
    cidades.append(cidade)

cidades.sort()

print("Cidades em ordem alfabética:")
for cidade in cidades:
    print(cidade)
````

- Altere o programa para trabalhar com 2 vetores. Além do vetor de cidade, adicione o vetor de população.

<hr>

## Exercício 3

- Teste o programa:

````
alturas = []

for i in range(5):
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    alturas.append(altura)

contador = 0
for altura in alturas:
    if altura > 1.80:
        contador += 1

print(f"{contador} pessoas têm altura superior a 1.80 metro.")
````
- Altere o programa para contar também as pessoas com menos de 1,50.

<hr>
