#2) Leia do usuário A e B e calcule: resultado2 = /seno(A) + seno(B)

import math

A = int(input('Insira o valor de A: '))
B = int(input('Insira o valor de B: '))

resultado = math.sqrt(math.sin(A) + math.sin(B))

print('O resultado da equação é:', round(resultado, 2))