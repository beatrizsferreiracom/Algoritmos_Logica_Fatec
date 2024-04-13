#9) Escreva um programa que leia o raio de um círculo do usuário e calcule sua área.

raio = float(input('Digite o raio do círculo em cm: '))

area = 3.1415 * (raio * raio)

print('A área do círculo é de ' + str(round(area, 2)) + ' cm².')