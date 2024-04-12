#2) Faça um programa que:
#Leia do usuário a nota1
#Leia do usuário a nota2
#Calcule a média como: media = nota1 * 0.5 + nota2 * 0.5
#Mostre a mensagem apropriada

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 * 0.5) + (nota2 * 0.5)

print('A média final é de ' + str(media) + ' pontos.')
