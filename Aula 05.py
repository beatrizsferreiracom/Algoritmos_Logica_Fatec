#EXERCÍCIOS DO DIA 14/03/2024

#1) Faça um programa qye leia A, B e C e calcule: resultado = /A² + B² + C²
import math

A = float(input('Insira o valor de A: '))
B = float(input('Insira o valor de B: '))
C = float(input('Insira o valor de C: '))

resultado = math.sqrt(A*A + B*B + C*C)

print('O resultado da equação é:', round(resultado, 2))
print('=====================================')
print('                                     ')


#2) Leia do usuário A e B e calcule: resultado2 = /seno(A) + seno(B)
import math

A = int(input('Insira o valor de A: '))
B = int(input('Insira o valor de B: '))

resultado = math.sqrt(math.sin(A) + math.sin(B))

print('O resultado da equação é:', round(resultado, 2))
print('=====================================')
print('                                     ')


#3) Leia A, B e C e calcule: resultado3 = /A + /B + /C
import math

A = float(input('Insira o valor de A: '))
B = float(input('Insira o valor de B: '))
C = float(input('Insira o valor de C: '))

resultado = math.sqrt(A) + math.sqrt(B) + math.sqrt(C)

print('O resultado da equação é:', round(resultado, 2))
print('=====================================')
print('                                     ')


#4) Faça um programa que leia do usuário:
#população atual, taxa de crescimento, anos
#Cacule: populaçãoFutura = populaçãoAtual * (1 + taxaDeCrescimento)^anos

import math

populacaoA = int(input('Digite a população atual: '))
taxaC = float(input('Digite a taxa de crescimento (5 para 5%): '))
anos = int(input('Insira a quantidade de anos: '))

populacaoF = populacaoA * math.pow((1 + (taxaC/100)), anos)

print('A população futura da cidade será de', populacaoF, 'pessoas.')
print('=====================================')
print('                                     ')


#5) Faça um programa que leia x1, x2, y1, y2, e calcule a distância entre os pontos A(x1,x2) B(y1,y2)
#distancia = /(x2-x1)^2 + (y2-y1)^2

import math

x1 = float(input('Insira o valor de x1: '))
x2 = float(input('Insira o valor de x2: '))
y1 = float(input('Insira o valor de y1: '))
y2 = float(input('Insira o valor de y2: '))

distancia = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))

print('A distância é de:', round(distancia,2))
print('=====================================')
print('                                     ')


#6) Cácule a diagonal de um triângulo. Leia a largura e comprimento:
#diagonal= /largura² + comprimento²

import math

largura = float(input('Digite o valor da largura, em cm: '))
comprimento = float(input('Digite o valor do comprimento, em cm: '))

diagonal = math.sqrt(largura**2 + comprimento**2)

print('O valor da diagonal é de', round(diagonal,2), 'centímentros.')
print('=====================================')
print('                                     ')

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
print('=====================================')
print('                                     ')


#Extra 1) Faça um programa que calcule a atração gravitacional de 2 objetos usando a massa e a distância.

# F = G * M * m / d²

#F: força gravitacional
#G: constante de gravitação universal
#M e m: massas dos corpos
#d: distância entre os centros de gravidade dos corpos


G = 6.67430e-11  # m^3 kg^-1 s^-2

massa1 = float(input("Digite a massa do primeiro objeto (em kg): "))
massa2 = float(input("Digite a massa do segundo objeto (em kg): "))
distancia = float(input("Digite a distância entre os objetos (em metros): "))

forca = G * massa1 * massa2 / distancia**2

print('A força de atração gravitacional entre os objetos é de ', forca, 'N')
