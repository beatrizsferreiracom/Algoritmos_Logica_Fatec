#Extra 3) Faça um programa que leia um valor em reais e mostre o total em:
#Dólares, euros, pesos, ienes

real = float(input('Insira o valor: R$'))

dolar = real / 4.93
euro = real / 5.40
pesos = real / 0.0058
iene = real / 0.033

print('O valor em dólares é: US$' + str(round(dolar, 2)))
print('O valor em euros é: €' + str(round(euro, 2)))
print('O valor em pesos é: AR$' + str(round(pesos, 2)))
print('O valor em ienes é: ¥' + str(round(iene, 2)))