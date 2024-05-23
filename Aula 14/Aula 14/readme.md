### EXERCÍCIOS DO DIA 16/05/2024

## Exercício 1

- Execute o seguinte programa e explique seu funcionamento:

````
vetor = [10, 20, 30, 40, 50]
for elemento in vetor:
    print(elemento)
````

<hr>

## Exercício 2

- Execute o seguinte programa e explique seu funcionamento:

````
vet_misto = [10, 3.14, "Python", 25, 2.71, "Programação"]
for elemento in vet_misto:
    print(elemento)
````

<hr>

## Exercício 3

- Execute o seguinte programa e explique seu funcionamento:

````
meu_vetor = [10, 'Python', -10.55, 0.0001, 50]

elemento_posicao_2 = meu_vetor[2]
print(elemento_posicao_2)

primeiro_elemento = meu_vetor[0]
print(primeiro_elemento)

ultimo_elemento = meu_vetor[-1]
print(ultimo_elemento)  

print('')
for elementos in meu_vetor:
    print(elementos)
````

<hr>

## Exercício 4

- Altere o programa adicionando um FOR para mostrar todos os elementos do vetor.

<hr>

## Exercício 5

- Aprimore o programa para não permitir o usuário informar um número que extrapole as dimensões do vetor.

<hr>

## Exercício 6

- Execute o seguinte programa e explique seu funcionamento:

````
tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho    #<---- o que é isso?

for i in range(tamanho):
    elemento = input(f"Digite o elemento {i+1}: ")
    vetor[i] = elemento

print("Vetor:", vetor)
````

<hr>

## Exercício 7

- Altere o programa para mostrar a média das notas dos alunos.

<hr>

## Exercício 8

- Explique o append, o sum e o len

````
notas = []

for i in range(5):
    nota = float(input(f"Digite a nota da disciplina {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média aritmética das notas é: {media:.2f}")
````
