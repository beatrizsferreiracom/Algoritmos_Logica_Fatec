#1) Faça um programa que leia 2 números (A, B) e troque seus valores entre si utilizando uma variável C.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

c = a
a = b
b = c

print('O novo valor de a é', a, 'e o novo valor de b é', b)
