#1) Escreva um programa que calcule a aceleração média de um objeto, dadas sua velocidade inicial, velocidade final e o tempo decorrido. 
#O programa deve solicitar ao usuário os valores de velocidade inicial, velocidade final e tempo, e exibir a aceleração média calculada.

velocidadeI = float(input('Digite a velocidade inicial (em m/s): '))
velocidadeF = float(input('Digite a velocidade final (em m/s): '))
tempo = float(input('Digite o tempo (em segundos): '))

aceleracao = (velocidadeF**2 - velocidadeI**2) / (2 * tempo)

print('A aceleração média é de', aceleracao, 'm/s²')
print('===============================')
print('                               ')


#2) Crie um programa que calcule o volume de uma esfera, dado seu raio. 
#O programa deve pedir ao usuário o valor do raio (r) e, em seguida, calcular o volume usando a fórmula:

raio = float(input("Digite o raio da esfera, em cm: ")) 
volume = (4/3) * 3.1415 * raio**3 

print("O volume da esfera é de", round(volume, 2), "cm³")
print('===============================')
print('                               ')


#3) Escreva um programa que calcule o valor futuro de um investimento, dado o valor inicial, a taxa de juros anual e o número de anos. 
#O programa deve solicitar ao usuário os valores de valor inicial, taxa de juros anual e número de anos, 
#e exibir o valor futuro calculado.

import math

valorI = float(input('Digite o valor inicial investido: R$'))
taxa = float(input('Digite a taxa de juros anual (eX: 5 para 5%): '))
anos = int(input('Digite o número de anos: '))

valorF = valorI * math.pow((1 + (taxa/100)), anos) 

print('O valor final do investimento é de R$' + str(round(valorF,2)))

