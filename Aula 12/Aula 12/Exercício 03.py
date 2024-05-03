#3) Faça um programa que:
#Leia do usuário o valor de N.
#Dentro do FOR leia o valor de idade e acumule a idade a variável soma.

soma = 0
quantidade = int(input('Digite quantas idades serão lidas '))

for i in range(quantidade):
    idade = int(input('Digite uma idade: '))
    soma += idade

print('A soma das idades é:', soma)