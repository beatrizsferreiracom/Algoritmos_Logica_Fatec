#1) Faça um programa que leia A, B e C e calcule: resultado = /A² + B² + C²

import math

A = float(input('Insira o valor de A: '))
B = float(input('Insira o valor de B: '))
C = float(input('Insira o valor de C: '))

resultado = math.sqrt(A*A + B*B + C*C)

print('O resultado da equação é:', round(resultado, 2))