#6) Faça um programa que leia: O total da compra, o valor do desconto, o valor dos juros
#Calcule a conta total: conta = total – desconto + juros

total = float(input('Insira o valor da compra: R$'))
desconto = float(input('Insira o valor do desconto: R$'))
juros = float(input('Insira o valor dos juros: R$'))

conta = total - desconto + juros

print('O valor total da conta é de: R$' + str(conta))
