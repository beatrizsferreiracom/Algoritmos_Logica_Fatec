#1) Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer no plano, 
#P(x1,y1) e P(x2,y2), escreva a distância entre eles.

import math

x1 = float(input('Insira o valor de x1: '))
x2 = float(input('Insira o valor de x2: '))
y1 = float(input('Insira o valor de y1: '))
y2 = float(input('Insira o valor de y2: '))

distancia = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))

print('A distância é de:', round(distancia,2))