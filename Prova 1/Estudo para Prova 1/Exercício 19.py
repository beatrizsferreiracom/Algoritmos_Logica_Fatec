#19) Um usuário deseja um algoritmo onde possa escolher que tipo de média deseja calcular a partir de 3 notas. 
#Faça um algoritmo que leia as notas, a opção escolhida pelo usuário e calcule a média.

#1 -aritmética
#2 -ponderada (3,3,4)
#3 -harmônica

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
tipo = int(input('Digite o tipo de média para o cálculo (1, 2 ou 3): '))

if tipo == 1:
    media = (nota1 + nota2 + nota3) / 3
elif tipo == 2:
    media = nota1 * 0.3 + nota2 * 0.3 + nota3 * 0.4
elif tipo == 3:
    media = 3 / ((1/nota1) + (1/nota2) + (1/nota3))
else:
    print('Opção inválida.')

print('A média final é de', round(media,2), 'pontos.')

