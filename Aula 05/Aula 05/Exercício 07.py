#7) Faça um programa que leia A, B, C, D e calcule:
# x = A² - /B²      y = C² + /D²    r = /(x + y)²

import math

A = float(input('Insira o valor de A: '))
B = float(input('Insira o valor de B: '))
C = float(input('Insira o valor de C: '))
D = float(input('Insira o valor de D: '))

x = A**2 - math.sqrt(B**2)
y = C**2 + math.sqrt(D**2) 
R = math.sqrt(math.pow(x+y, 2))

print('O valor de x é: ', x)
print('O valor de y é: ', y)
print('O valor de R é: ', R)