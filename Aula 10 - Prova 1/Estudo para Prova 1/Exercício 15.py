#15) Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando 
#se este número é par ou ímpar, e se é positivo ou negativo.

numero = int(input('Digite o número: '))

if numero % 2 == 0:
    if numero > 0:
        print('O número é par e positivo.')
    elif numero < 0:
        print('O número é par e negativo.')
    else:
        print('O número é neutro: 0')

else:
    if numero > 0:
        print('O número é ímpar e positivo.')
    elif numero < 0:
        print('O número é ímpar e negativo.')
    else:
        print('O número é neutro: 0')