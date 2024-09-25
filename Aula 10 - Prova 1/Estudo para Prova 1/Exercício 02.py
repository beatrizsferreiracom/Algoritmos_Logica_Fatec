#2) Escreva um algoritmo que leia três números inteiros e positivos (A, B, C) e calcule a expressão:

import math 

A = int(input('Insira o valor de A: '))
B = int(input('Insira o valor de B: '))
C = int(input('Insira o valor de C: '))

R = math.pow(A+B,2)
S = math.pow(B+C,2)
D = (R + S) / 2

print('O valor final é', round(D,2))