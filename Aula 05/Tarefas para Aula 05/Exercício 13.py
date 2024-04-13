#13) Escreva um programa que leia uma distância em metros do usuário 
#e a converta para centímetros, quilômetros e milímetros

metros = float(input('Digite a distância percorrida em metros: '))

centimetros = metros * 100
milimetros = metros * 1000
quilometros = metros / 1000

print('A distância percorrida em centímetros:', centimetros, 'cm')
print('A distância percorrida em milímetros:', milimetros, 'mm')
print('A distância percorrida em quilômetros:', quilometros, 'km')