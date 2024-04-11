#4) Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

dias = int(input('Insira a idade em dias: '))
anos = dias / 365
meses = dias / 30

print('A idade é de', round(anos), 'anos,', round(meses), 'meses e', dias, 'dias.')
