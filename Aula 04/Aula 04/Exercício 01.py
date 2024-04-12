#1)Faça um um programa que:
#Leia do usuário o raio do círculo
#Calcule área: area = 3,1415 * raio * raio
#Mostre a área com mensagem apropriada

raio = float(input('Digite o raio do círculo em cm: '))

area = 3.1415 * (raio * raio)

print('A área do círculo é de ' + str(area) + ' cm².')