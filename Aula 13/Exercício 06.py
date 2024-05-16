#6) Faça um programa que leia vários números do usuário até que ele informe o número 0 (zero) para terminar.

numero = int(input('Digite um número: '))

while numero != 0:
    numero = int(input('Digite outro número: '))

print('Programa finalizado.')