#1) Escreva um programa que calcule a aceleração média de um objeto, dadas sua velocidade inicial, velocidade final e o tempo decorrido. 
#O programa deve solicitar ao usuário os valores de velocidade inicial, velocidade final e tempo, e exibir a aceleração média calculada.

velocidadeI = float(input('Digite a velocidade inicial (em m/s): '))
velocidadeF = float(input('Digite a velocidade final (em m/s): '))
tempo = float(input('Digite o tempo (em segundos): '))

aceleracao = (velocidadeF**2 - velocidadeI**2) / (2 * tempo)

print('A aceleração média é de', aceleracao, 'm/s²')