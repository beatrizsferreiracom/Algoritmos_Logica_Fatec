#4) Leia o total e a série da nota fiscal:

total = float(input('Digite o total da nota fiscal: R$'))
serie = input("Digite a série da nota fiscal: ")


if serie == 'E1':
    if total > 180:
        imposto = total * 0.17
    else:
        imposto = total * 0.14
else:
    if total > 199:
        imposto = total * 0.18
    else:
        imposto = total * 0.16

print('A nota fiscal série ' + serie + ' terá imposto de R$' + str(round(imposto)))