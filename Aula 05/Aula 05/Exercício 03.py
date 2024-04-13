#3) Leia A, B e C e calcule: resultado3 = /A + /B + /C

import math

A = float(input('Insira o valor de A: '))
B = float(input('Insira o valor de B: '))
C = float(input('Insira o valor de C: '))

resultado = math.sqrt(A) + math.sqrt(B) + math.sqrt(C)

print('O resultado da equação é:', round(resultado, 2))