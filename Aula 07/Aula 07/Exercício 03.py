#3) Leia o preço do produto e mostre o valor do desconto.

preco = float(input('Digite o preço do produto: '))

if preco < 50.00:
    print('Seu desconto foi de 10% e o valor total é de R$' + str(preco * 0.9))
else:
    print('Seu desconto foi de 20% e o valor total é de R$' + str(preco * 0.8))