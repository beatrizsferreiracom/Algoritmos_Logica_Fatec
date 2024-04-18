#5) Leia os valores do aluguel, a área e o total:

aluguel = float(input('Digite o valor do aluguel: R$'))
area = float(input('Digite a área, em m²: '))
total = float(input('Digite o valor total: R$'))

if area > 50:
    if total > 350000:
        if aluguel > 1800:
            preco = aluguel * 12 + total
        else:
            preco = aluguel * 6 + total
    else:
        preco = aluguel + total
else:
    preco = total * 1.12

print('O valor total a ser pago é de R$' + str(round(preco,2)))