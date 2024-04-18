#2) Leia o saldo e dias:

saldo = float(input('Digite o saldo: R$'))
dias = int(input('Digite o número de dias: '))

if saldo < 0:
    if dias < 30:
        saldo = saldo * 1.04
    if dias > 30:
        saldo = saldo + (0.8)**dias
else:
    if dias < 30:
        saldo = saldo * 1.08
    if dias > 30:
        saldo = saldo + (0.7)**dias

print("O saldo atual é de R$", round(saldo, 2))