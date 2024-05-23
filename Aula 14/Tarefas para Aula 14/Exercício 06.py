#6) Faça um programa que: 
#Leia o valor de N. 
#Dentro do laço de repetição, leia N totais de vendas e faça os somatórios desses totais. 
#Mostre o imposto.

contador = 1
soma = 0
quantidade = int(input('Insira a quantidade de vendas: '))

while(quantidade >= contador):
    vendas = float(input('Insira o total da venda: R$'))
    contador += 1
    soma += vendas

if vendas > 500:
    imposto = soma * 0.15
else:
    imposto = soma * 0.11

print('O imposto é de R$' + str(round(imposto, 2)))
