#4) Leia o salário do funcionário e calcule:

salario = float(input('Digite seu salário: R$'))

beneficio = salario * 0.1
desconto = salario * 0.06
total = salario + beneficio - desconto

if total < 1500:
    print('O imposto é de 0% e o salário é de R$' + str(round(total)))
else:
    print('O imposto é de 10% e o salário é de R$' + str(round(total * 1.1)))