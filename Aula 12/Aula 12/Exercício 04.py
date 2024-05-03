#4) Faça um programa que leia do usuário um valor de N.
#Em seguida, com o FOR, leia N notas e calcula a sua somatória.
#Ao final, mostre e média das notas.
#E também faça um IF para mostrar
#Aprovado se a média for maior que 7.
#Reprovado caso contrário.

soma = 0
quantidade = int(input('Digite quantas notas serão lidas: '))

for i in range(quantidade):
    notas = float(input('Digite uma nota: '))
    soma += notas

media = soma/quantidade

if media > 7:
    print('A média é de', round(media,2), 'pontos e o aluno foi aprovado.')
else:
    print('A média é de', round(media,2), 'pontos e o aluno foi reprovado.')