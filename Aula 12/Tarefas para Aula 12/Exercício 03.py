#3) Escreva um programa que leia o nome do usuário e um número e mostre o nome do usuário a 
#quantidade de vezes de acordo com o número. Mostre assim: 

#1 - Nome
#2 - Nome
#3 - Nome
#...

nome = input('Digite o nome: ')
numero = int(input('Digite o número de repetições: '))

for i in range(numero):
    print(nome)