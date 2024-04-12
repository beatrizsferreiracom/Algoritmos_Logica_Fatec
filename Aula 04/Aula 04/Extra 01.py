#Extra 1: Faça um programa que leia do usuário a temperatura em Celsius e mostre em Fahrenheit.

celsius = float(input('Insira a temperatura em graus Celsius: '))

fah = (celsius * 1.8) + 32

print('A temperatura em Fahrenheit é de ' + str(fah) + '°F')
