#4) Faça um programa que leia o total da conta do restaurante.
#Calcule a gorjeta de 10%: gorjeta = total * 10/100
#Calcule a conta com a gorjeta: conta = total + gorjeta
#Mostre o resultado

total = float(input('Insira o valor da conta: R$'))
gorjeta = total * (10/100)
conta = total + gorjeta

print('O valor a ser pago é: R$' + str(round(conta, 2)))