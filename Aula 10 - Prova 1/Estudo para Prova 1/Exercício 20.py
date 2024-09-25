#20) Um vendedor necessita de um algoritmo que calcule o preço total devido por um cliente. O algoritmo deve receber 
#o código de um produto e a quantidade comprada e calcular o preço total,usando a tabela abaixo:

#Código do Produto     Preço unitário
#1001                      5,32
#1324                      6,45
#6548                      2,37
#9870                      5,32
#7623                      6,45

codigo = int(input('Digite o código do item: '))
quantidade = int(input('Digite a quantidade do item: '))

if codigo == 1001:
    valor = 5.32 * quantidade
elif codigo == 1324:
    valor = 6.45 * quantidade
elif codigo == 6548:
    valor = 2.37 * quantidade
elif codigo == 9870:
    valor = 5.32 * quantidade
elif codigo == 7623:
    valor = 6.45 * quantidade
else:
    print('Código inválido!')

print('O valor total a ser pago é de R$' + str(round(valor, 2)))