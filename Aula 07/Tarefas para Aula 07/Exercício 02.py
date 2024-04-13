#2) Escreva um programa que leia uma string e determine se ela está vazia ou não.

string = input('Digite a string: ')

if len(string) == 0:
    print('A string está vazia.')
else:
    print('A string não está vazia.')