#8) Leia total e itens:

itens = int(input('Digite a quantidade de itens: '))
total = float(input('Digite o total da compra: R$'))

if itens > 10 and total > 100:
    desconto = total * 0.15
else:
    desconto = total * 0.06

compra = total - desconto

print('O valor do desconto será de R$' + str(round(desconto,2)) + ' e o valor final será de R$' + str(round(compra,2)))