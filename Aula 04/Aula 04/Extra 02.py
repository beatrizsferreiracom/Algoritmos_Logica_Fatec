#Extra 2: Faça uma programa que calcule Δ da fórmula de Bhaskara:
#Δ = b² = 4ac

A = float(input('Insira o valor de A: '))
B = float(input('Insira o valor de B: '))
C = float(input('Insira o valor de C: '))

bhaska = (B * B) - 4 * A * C

print('O valor de Δ é: ' + str(bhaska))