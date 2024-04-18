#1) Leia a idade e altura:

idade = int(input('Digite a idade: '))
altura = int(input('Digite a altura, em cm: '))

if idade > 17:
    if altura > 160:
        bolsa = 1120
    else:
        bolsa = 1410
else:
    bolsa = 1439

print('A bolsa será de R$' + str(bolsa))