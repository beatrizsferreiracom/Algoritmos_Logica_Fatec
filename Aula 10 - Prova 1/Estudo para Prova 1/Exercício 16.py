#16) O cardápio de uma lancheria é o seguinte:

#Especificação     Código     Preço
#Cachorro quente    100       1,20
#Bauru simples      101       1,30
#Bauru com ovo      102       1,50
#Hambúrger          103       1,20
#Cheeseburguer      104       1,30
#Refrigerante       105       1,00

#Escreva um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche. 
#Considere que a cada execução somente será calculado um item.

codigo = int(input('Digite o código do item: '))
quantidade = int(input('Digite a quantidade do item: '))

if codigo == 100:
    valor = 1.20 * quantidade
elif codigo == 101:
    valor = 1.30 * quantidade
elif codigo == 102:
    valor = 1.50 * quantidade
elif codigo == 103:
    valor = 1.20 * quantidade
elif codigo == 104:
    valor = 1.30 * quantidade
elif codigo == 105:
    valor = 1.00 * quantidade
else:
    print('Código inválido!')

print('O valor total da compra é de R$' + str(round(valor, 2)))