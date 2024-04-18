#4) Escreva um programa que solicite ao usuário um número inteiro positivo. Em seguida, verifique 2 números que 
#divididos resulte o número que o usuário informou. Por exemplo, 6 é a divisão de 12 por 2.

numero = int(input('Insira um número inteiro e positivo: '))

valor1 = numero * 2
valor2 = numero * 3
valor3 = numero * 4
valor4 = numero * 5

print('Para chegar ao valor', numero, 'podemos dividir', valor1, 'por dois.')

print('Outras opções:')
print('Dividir', valor2, 'por três.')
print('Dividir', valor3, 'por quatro.')
print('Dividir', valor4, 'por cinco.')