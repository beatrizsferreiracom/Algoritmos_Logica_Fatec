#EXERCÍCIOS DO DIA 21/03/2024

#1) Crie um programa que leia a idade e, usando a condicional, retorne a mensagem adequada.

idade = int(input('Informe sua idade: '))

if idade >17:
    print('Maior de idade')
else:
    print('Menor de idade')
print('=====================================')
print('                                     ')


#2) Crie um programa que leia a nota do aluno.(float). 
#Dê a mensagem "aprovado" se nota >=6. Se não, dê mensagem "reprovado"

nota = float(input('Digite sua nota: '))

if nota >=6:
    print('Aprovado')
else:
    print('Reprovado')
print('=====================================')
print('                                     ')


#3) Crie um programa que leia a senha do usuário.

senha = input('Digite a senha: ')

if senha == 'Aluno123':
    print('Senha correta.')
else:
    print('Senha incorreta.')
print('=====================================')
print('                                     ')


#4) Crie um programa que leia o salário do funcionário:

salario = float(input('Digite o salário: R$'))

if salario >4900:
    print('Imposto de 15%')
else:
    print('Imposto de 5%')
print('=====================================')
print('                                     ')
