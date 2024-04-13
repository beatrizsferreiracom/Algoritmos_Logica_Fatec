#1) Crie um programa que leia x1 e x2 e veja a inclinação:

x1 = float(input('Digite o primeiro número: '))
x2 = float(input('Digite o segundo número: '))

alfa = x1**2 + x2**2

if alfa > 1.0:
    print('Inclinação positiva.')
else:
    print('Inclinação negativa.')