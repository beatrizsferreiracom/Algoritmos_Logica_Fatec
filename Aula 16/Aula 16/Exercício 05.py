#5) Criar um programa que leia o valor de N do usuário, leia N nomes (sem append).
#Em seguida, mostre os nomes que estão em posições pares (mostre também a posição)
#Depois, mostre os outros nomes que estão em posições impares (a posicão também)

quantidade = int(input("Informe a quantidade de nomes: "))

vetor = [0] * quantidade

for i in range(quantidade):
    nome = str(input(f"Digite o {i+1}º nome: "))
    vetor[i] = nome

print('\nPosições ímpares')
for i in range(len(vetor)):
    if i % 2 != 0:
        print('Posição', i, 'Nome:', vetor[i])

print('\nPosições pares')
for i in range(len(vetor)):
    if i % 2 == 0:
        print('Posição', i, 'Nome:', vetor[i])