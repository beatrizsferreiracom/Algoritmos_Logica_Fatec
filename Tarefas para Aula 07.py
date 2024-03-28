#1) Desenvolva um programa que leia um número inteiro e verifique se ele é divisível por 3. Pesquise o operador %.

numero = int(input('Digite um número inteiro: '))

if numero % 3 == 0:
    print('O número', numero, 'é divisível por 3')
else:
    print('O número', numero, 'não é divisível por 3')
print('===============================')
print('                               ')


#2) Escreva um programa que leia uma string e determine se ela está vazia ou não.

string = input('Digite a string: ')

if len(string) == 0:
    print('A string está vazia.')
else:
    print('A string não está vazia.')
print('===============================')
print('                               ')

#3) Crie um programa que leia duas notas de um aluno e calcule sua média. 
#Se a média for maior ou igual a 7, o aluno foi aprovado. 
#Caso contrário, o aluno foi reprovado.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('A média é de', media, 'pontos e o aluno foi aprovado!')
else:
    print('A média é de', media, 'pontos e o aluno foi reprovado!')