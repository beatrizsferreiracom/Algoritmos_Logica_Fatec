#22) Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo. 
#Faça um algoritmo que leia o salário e o cargo de um funcionário e calcule o novo salário. Se o cargo do funcionário não  estiver 
#na tabela, ele deverá, então, receber 40% de aumento. Mostre o salário antigo, o novo salário e a diferença.

#Código    Cargo    Percentual
#101      Gerente      10%
#102     Engenheiro    20%
#103      Técnico      30%

codigo = int(input('Digite o código do cargo: '))
salario = int(input('Digite o salário: R$'))

if codigo == 101:
    valor = salario * 0.1
elif codigo == 102:
    valor = salario *  0.2
elif codigo == 103:
    valor = salario * 0.3
else:
    valor = salario * 0.4

total = salario + valor

print('O salário antigo era de R$' + str(salario) + '. O novo sálario é de R$'+ str(round(total,2)))
print('A diferença é de R$' + str(total - salario))