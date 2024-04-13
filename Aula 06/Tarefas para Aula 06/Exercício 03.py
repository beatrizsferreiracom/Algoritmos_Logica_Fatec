#3) Escreva um programa que calcule o valor futuro de um investimento, dado o valor inicial, a taxa de juros anual e o número de anos. 
#O programa deve solicitar ao usuário os valores de valor inicial, taxa de juros anual e número de anos, 
#e exibir o valor futuro calculado.

import math

valorI = float(input('Digite o valor inicial investido: R$'))
taxa = float(input('Digite a taxa de juros anual (eX: 5 para 5%): '))
anos = int(input('Digite o número de anos: '))

valorF = valorI * math.pow((1 + (taxa/100)), anos) 

print('O valor final do investimento é de R$' + str(round(valorF,2)))