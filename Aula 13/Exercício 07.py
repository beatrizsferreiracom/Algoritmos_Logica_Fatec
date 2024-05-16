#7) Crie um programa que leia número do usuário até que seja informado um número PAR.
#Dê mensagens ao usuário apropriadas para que ela saiba o que fazer e o que está acontecendo no programa.

numero = int(input('Digite um número: '))

while numero % 2 != 0:
    numero = int(input('Digite outro número: '))

print('Número par digitado. Programa finalizado.')