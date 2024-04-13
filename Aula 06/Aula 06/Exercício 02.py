#2) Crie um programa que leia a nota do aluno.(float). 
#Dê a mensagem "aprovado" se nota >=6. Se não, dê mensagem "reprovado"

nota = float(input('Digite sua nota: '))

if nota >=6:
    print('Aprovado')
else:
    print('Reprovado')