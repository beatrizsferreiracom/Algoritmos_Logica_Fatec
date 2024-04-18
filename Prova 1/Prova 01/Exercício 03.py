#3) Faça um programa que leia 3 números (A, B, C) e mostre o maior 
#número par e o maior número ímpar.

A = int(input('Insira o valor de A: '))
B = int(input('Insira o valor de B: '))
C = int(input('Insira o valor de C: '))

if A == B == C:
    if A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        print('Os números são iguais e pares.')
    else:
        print('Os números são iguais e ímpares.')


elif A > B > C:
    if A % 2 == 0 and B % 2 != 0 and C % 2 == 0:
        print('A é o maior número par e B é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 == 0 and C % 2 != 0:
        print('A é o maior número par e C é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 == 0:
        print('B é o maior número par e A é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 != 0 and C % 2 == 0:
        print('C é o maior número par e A é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 != 0:
        print('B é o maior número par e A é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 != 0 and C % 2 != 0:
        print('A é o maior número par e B é o maior número ímpar.')
    

elif A > C > B:
    if A % 2 == 0 and B % 2 != 0 and C % 2 == 0:
        print('A é o maior número par e B é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 == 0 and C % 2 != 0:
        print('A é o maior número par e C é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 == 0:
        print('C é o maior número par e A é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 != 0 and C % 2 == 0:
        print('C é o maior número par e A é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 != 0:
        print('B é o maior número par e A é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 != 0 and C % 2 != 0:
        print('A é o maior número par e C é o maior número ímpar.')


elif B > A > C:
    if A % 2 == 0 and B % 2 != 0 and C % 2 == 0:
        print('A é o maior número par e B é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 == 0 and C % 2 != 0:
        print('B é o maior número par e C é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 == 0:
        print('B é o maior número par e A é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 != 0 and C % 2 == 0:
        print('C é o maior número par e B é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 != 0:
        print('B é o maior número par e A é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 != 0 and C % 2 != 0:
        print('A é o maior número par e B é o maior número ímpar.')


elif B > C > A:
    if A % 2 == 0 and B % 2 != 0 and C % 2 == 0:
        print('C é o maior número par e B é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 == 0 and C % 2 != 0:
        print('B é o maior número par e C é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 == 0:
        print('B é o maior número par e A é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 != 0 and C % 2 == 0:
        print('C é o maior número par e B é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 != 0:
        print('B é o maior número par e C é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 != 0 and C % 2 != 0:
        print('A é o maior número par e B é o maior número ímpar.')


elif C > A > B:
    if A % 2 == 0 and B % 2 != 0 and C % 2 == 0:
        print('C é o maior número par e B é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 == 0 and C % 2 != 0:
        print('A é o maior número par e C é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 == 0:
        print('C é o maior número par e A é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 != 0 and C % 2 == 0:
        print('C é o maior número par e A é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 != 0:
        print('B é o maior número par e C é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 != 0 and C % 2 != 0:
        print('A é o maior número par e C é o maior número ímpar.')


elif C > B > A:
    if A % 2 == 0 and B % 2 != 0 and C % 2 == 0:
        print('C é o maior número par e B é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 == 0 and C % 2 != 0:
        print('B é o maior número par e C é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 == 0:
        print('C é o maior número par e A é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 != 0 and C % 2 == 0:
        print('C é o maior número par e B é o maior número ímpar.')
    elif A % 2 != 0 and B % 2 == 0 and C % 2 != 0:
        print('B é o maior número par e C é o maior número ímpar.')
    elif A % 2 == 0 and B % 2 != 0 and C % 2 != 0:
        print('A é o maior número par e C é o maior número ímpar.')



