#6) Faça um programa que:
#Leia o valor de N.
#Dentro do FOR, leia N totais de vendas e faça os somatórios desses totais.
#Fora do FOR, calcule e mostre o imposto.

soma = 0
quantidade = int(input('Insira a quantidade de vendas: '))

for i in range(quantidade):
    vendas = float(input('Insira o total da venda: R$'))
    soma += vendas

if vendas > 500:
    imposto = soma * 0.15
else:
    imposto = soma * 0.11

print('O imposto é de R$' + str(round(imposto, 2)))
