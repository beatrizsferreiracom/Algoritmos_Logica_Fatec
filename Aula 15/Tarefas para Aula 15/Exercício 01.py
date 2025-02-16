#1) Altere o programa para trabalhar com o vetor de nomes de alunos junto com o vetor de notas de alunos.

nomes = []
notas = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    nomes.append(nome)
    notas.append(nota)

maiorNota = max(notas)
menorNota = min(notas)

maior = notas.index(maiorNota)
menor = notas.index(menorNota)

nomeMaior = nomes[maior]
nomeMenor = nomes[menor]

print(f"A maior nota é: {maiorNota} do aluno {nomeMaior}")
print(f"A menor nota é: {menorNota} do aluno {nomeMenor}")

