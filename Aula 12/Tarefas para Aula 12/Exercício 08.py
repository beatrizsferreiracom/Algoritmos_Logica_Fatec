#8) Faça um algoritmo que leia 10 números do usuário e mostre quantos são pares.

pares = 0

for i in range(10):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares += 1

print(pares, 'números são pares.')