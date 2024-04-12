#7) Faça um programa que leia uma distância em metros e mostre: 
#Em centímetros, em milímetros

metro = float(input('Digite a distância percorrida: '))

centimetros = metro * 100
milimetros = metro * 1000

print('A distância percorrida é de ' + str(centimetros) + ' centímetros ou ' + str(milimetros) + ' milímetros.' )