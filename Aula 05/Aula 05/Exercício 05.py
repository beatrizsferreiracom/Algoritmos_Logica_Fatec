#5) Faça um programa que leia x1, x2, y1, y2, e calcule a distância entre os pontos A(x1,x2) B(y1,y2)
#distancia = /(x2-x1)^2 + (y2-y1)^2

import math

x1 = float(input('Insira o valor de x1: '))
x2 = float(input('Insira o valor de x2: '))
y1 = float(input('Insira o valor de y1: '))
y2 = float(input('Insira o valor de y2: '))

distancia = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))

print('A distância é de:', round(distancia,2))