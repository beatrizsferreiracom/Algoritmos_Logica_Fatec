#5) Um programa de adivinhação
#Faça um programa que tenha um while (numero != 55) e dentro do while peça para o usuário tentar adivinhar um número. 
#O laço deve continuar até o usuário adivinhar que o número é o 55.

numero = int(input('Digite um número: '))

while numero != 55:
    print('Número incorreto.')
    numero = int(input('Digite novamente: '))

print('Você acertou!')