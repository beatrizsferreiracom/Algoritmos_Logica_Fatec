#6) Faça um Programa que leia N números inteiros (pergunte para o usuário o valor de N) e armazene-os num vetor. 
#Depois, utilize um for para armazene os números pares no vetor VETPAR e os números ímpares no vetor VETIMPAR. 
#Ao final, faça FOR para imprimir cada um dos 3 três vetores.

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = []
pares = []
impares = []

for i in range(tamanho):
    num = int(input(f"Digite o número {i+1}: "))
    vetor.append(num)

for i in vetor:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("Números do vetor:", vetor)
print("Números pares:", pares)
print("Números ímpares:", impares)