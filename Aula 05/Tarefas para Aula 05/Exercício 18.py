#18) Faça um programa que leia do usuário o seu salário e calcule:
#-imposto = salario *0.15
#-inss = salario*0.17
#-valor = salario - imposto - inss

salario = float(input('Digite o salário: R$'))
imposto = salario * 0.15
inss = salario * 0.17
valor = salario - imposto - inss

print('O valor do salário líquido é de: R$' + str(valor))