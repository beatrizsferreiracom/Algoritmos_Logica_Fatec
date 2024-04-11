#21) Um vendedor precisa de um algoritmo que calcule o preço total devido por um cliente. O algoritmo deve receber o código
#de um produto e a quantidade comprada e calcular o preço total, usando a tabela abaixo. Mostre uma mensagem no caso de código inválido.

#Código      #Preço unitário
#'ABCD'         R$ 5,30
#'XYPK'         R$ 6,00
#'KLMP'         R$ 3,20
#'QRST'         R$ 2,50


codigo = input('Digite o código do item: ')
quantidade = int(input('Digite a quantidade do item: '))

if codigo == 'ABCD':
    valor = 5.30 * quantidade
elif codigo == 'XYPK':
    valor = 6.00 * quantidade
elif codigo == 'KLPM':
    valor = 3.20 * quantidade
elif codigo == 'QRST':
    valor = 2.50 * quantidade
else:
    print('Código inválido!')

print('O valor total a ser pago é de R$' + str(round(valor,2)))