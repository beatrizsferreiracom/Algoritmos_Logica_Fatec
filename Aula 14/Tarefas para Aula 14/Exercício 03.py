#3) Faça um programa que: Leia do usuário o valor de N. Dentro laço leia o valor de idade e acumule a idade a variável soma.

contador = 1
soma = 0
quantidade = int(input('Digite quantas idades serão lidas: '))

while (quantidade >= contador):
    idade = int(input('Digite uma idade: '))
    contador += 1
    soma += idade

print('A soma das idades é:', soma)