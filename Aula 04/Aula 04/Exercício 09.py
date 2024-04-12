#9) Faça um programa que leia do usuário o salário.
#Calcule: imposto = salario * 0.15
#Calcule: inss = salario * 0.17
#Calcule: valor = salario – imposto – inss
#Mostrar a mensagem adequada

salario = float(input('Digite o salário: R$'))

imposto = salario * 0.15
inss = salario * 0.17
valor = salario - imposto - inss

print('O valor do salário líquido é de: R$' + str(valor))