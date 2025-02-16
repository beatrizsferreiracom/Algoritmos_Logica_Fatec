#1) Crie um programa que leia N do usuário. Depois, faça um FOR para ler N números inteiros do usuário
#Em seguida, faça um outro FOR para mostrar os números e as respectivas posições, somente daqueles que estão em posições pares.

vetor = []

quantidade = int(input("Informe a quantidade de números: "))

for i in range(quantidade):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

for i in range(len(vetor)):
    if i % 2 == 0:
        print(f'Posição {i}, número {vetor[i]}')