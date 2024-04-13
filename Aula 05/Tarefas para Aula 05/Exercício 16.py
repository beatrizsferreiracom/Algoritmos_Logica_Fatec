#16) Escreva um programa que leia um valor em dólares (USD) do usuário e o converta 
#para euros (EUR) e reais (BRL), considerando taxas de câmbio fixas

valorD = float(input("Digite o valor em dólares (USD): "))

#Taxas de câmbio fixas
taxaE = 0.92  # 1 USD = 0.92 EURO
taxaR = 4.98  # 1 USD = 4.98 REAL

valorE = valorD * taxaE
valorR = valorD * taxaR

print('O valor em dólares, US$' + str(valorD) + ', é igual a:')
print('€' + str(round(valorE, 2)))
print('R$' + str(round(valorR, 2)))