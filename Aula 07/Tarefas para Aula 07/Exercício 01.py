#1) Desenvolva um programa que leia um número inteiro e verifique se ele é divisível por 3. Pesquise o operador %.

numero = int(input('Digite um número inteiro: '))

if numero % 3 == 0:
    print('O número', numero, 'é divisível por 3')
else:
    print('O número', numero, 'não é divisível por 3')