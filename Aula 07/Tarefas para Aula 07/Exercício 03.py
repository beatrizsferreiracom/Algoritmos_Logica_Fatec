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