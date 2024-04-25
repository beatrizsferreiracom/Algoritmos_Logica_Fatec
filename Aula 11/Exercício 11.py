#Faça um programa que leia a idade de 5 pessoas e exiba a soma das idades.

#Dica:
#inicialize a variável soma=0
#faça o for de 1 a 6
#dentro do for leia a idade
#soma a idade soma+=idade
#fora do for, mostre a soma

soma = 0
for i in range(1, 6): 
    idade = int(input('Digite a idade: '))
    soma += idade

print('A soma das idades é:', soma)