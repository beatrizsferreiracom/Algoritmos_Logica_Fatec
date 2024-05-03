#5) Faça um programa que leia a idade de 20 pessoas e exiba a soma das idades.

soma = 0
for i in range(20): 
    idade = int(input('Digite uma idade: '))
    soma += idade

print('A soma das idades é:', soma)