#3) Faça um programa que leia
#Nota do TCC, Nota da prova, Nota do trabalho
#Calcule a media: TCC * 0.3 + prova * 0.5 + trabalho * 0.2

TCC = float(input('Digite a nota do TCC: '))
prova = float(input('Digite a nota da prova: '))
trab = float(input('Digite a nota do trabalho: '))

media = (TCC * 0.3) + (prova * 0.5) + (trab * 0.2)

print('A média final foi de ' + str(media) + ' pontos.')