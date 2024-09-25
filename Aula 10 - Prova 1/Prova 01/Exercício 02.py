#2) Crie um programa que leia o ano de nascimento de uma pessoa e o ano atual. Calcule e mostre qual é: 
#a idade da pessoa em anos; a idade da pessoa em horas; a idade da pessoa em minutos; a idade da pessoa em semanas.

anoA = int(input('Insira o ano atual: '))
anoN = int(input('Insira o ano de nascimento: '))

anos = anoA - anoN
meses = anos * 12
semanas = meses * 4
dias = anos * 365
horas = dias * 24
minutos = horas * 60

print('A idade é de', anos, 'anos,', horas, 'horas,', minutos, 'minutos e', semanas, 'semanas.')