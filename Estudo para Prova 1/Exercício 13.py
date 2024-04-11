#13) Escreva um algoritmo que leia 3 números inteiros e mostre o maior deles.

a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))
c = int(input('Insira o valor de C: '))

if a > b and a > c:
    print('O valor de A,', a, ', é o maior.')
elif b > a and b > c:
    print('O valor de B,', b, ', é o maior.')
elif c > a and c > b:
    print('O valor de C,', c, ', é o maior.')
else:
    print('Os valores de A, B e C são iguais:', a)