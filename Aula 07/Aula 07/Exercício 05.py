#5) Leia do usuário sua idade, leia do valor do plano de saúde.

idade = int(input("Digite sua idade: "))
plano = float(input('Digite o valor do plano de saúde: R$'))

if idade >= 60:
    print('O novo valor do plano é: R$' + str(round(plano*1.22)))
else:
    print('O novo valor do plano é: R$' + str(round(plano*1.06)))