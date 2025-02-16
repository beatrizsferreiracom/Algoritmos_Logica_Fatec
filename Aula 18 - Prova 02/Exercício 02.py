#2) Encontrar o maior e o menor elemento sem utilizar funções prontas Python
#Escreva um programa que leia um vetor de tamanho N (informado pelo usuário) e encontre o maior e o menor elemento do vetor.
#O programa deve imprimir esses dois valores.

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho

for i in range(tamanho):
    valor = float(input(f"Digite o {i+1}º valor: "))
    vetor[i] = valor

maior = vetor[0]
menor = vetor[0]

for i in range(1, tamanho):
    if vetor[i] > maior:
        maior = vetor[i]
    elif vetor[i] < menor:
        menor = vetor[i]

print("Maior elemento:", maior)
print("Menor elemento:", menor)




