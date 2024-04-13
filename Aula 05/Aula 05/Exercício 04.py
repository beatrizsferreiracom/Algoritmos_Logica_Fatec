#4) Faça um programa que leia do usuário:
#população atual, taxa de crescimento, anos
#Cacule: populaçãoFutura = populaçãoAtual * (1 + taxaDeCrescimento)^anos

import math

populacaoA = int(input('Digite a população atual: '))
taxaC = float(input('Digite a taxa de crescimento (5 para 5%): '))
anos = int(input('Insira a quantidade de anos: '))

populacaoF = populacaoA * math.pow((1 + (taxaC/100)), anos)

print('A população futura da cidade será de', populacaoF, 'pessoas.')