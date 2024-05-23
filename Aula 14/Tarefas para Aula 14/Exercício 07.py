#7) ) Faça um programa que:
#Leia o valor de N.
#Faça o laço de repetição para ler N vezes: 
#Valor da compra com CARTAO e faça somatória SOMACARTAO.
#Valor da compra com DINHEIRO e faça somatória SOMADINHEIRO.
#Ao final do laço de repetição, mostre os valores das 2 somatórias.


contador = 1
somaCartao = 0
somaDinheiro = 0

quantidade = int(input('Insira a quantidade de compras: '))

while(quantidade >= contador):
    valor = float(input('Insira o valor da compra: '))
    tipo = input('Insira a forma de pagamento: ')
    contador += 1

    if tipo == 'Dinheiro':
      somaDinheiro += valor
    elif tipo == 'Cartão':
      somaCartao += valor

print('O valor a ser pago no dinheiro é de R$', somaDinheiro, 'e no cartão é de R$', somaCartao)
