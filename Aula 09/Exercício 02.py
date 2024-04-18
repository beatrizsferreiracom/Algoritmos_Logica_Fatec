#2) Faça um programa que leia 3 valores e mostre o maior deles utilizando if.

a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))

if a > b and a > c:
    print('O valor de a é o maior:', a)
elif b > a and b > c:
    print('O valor de b é o maior:', b)
elif c > a and c > b:
    print('O valor de c é o maior:', c)