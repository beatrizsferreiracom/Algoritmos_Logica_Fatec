#9) Escreva um programa que leia 10 números do usuário e mostre o maior deles.

maior = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero

print(maior, 'é o maior número.')