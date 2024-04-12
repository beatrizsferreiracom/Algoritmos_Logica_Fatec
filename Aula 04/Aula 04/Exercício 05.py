#5) Faça um programa que leia: peso, altura
#Calcule o IMC = peso : altura²

peso = float(input('Digite so peso em kg: '))
altura = float(input('Digite a altura em m: '))

imc = peso / (altura * altura)

print('O valor do IMC é: ' + str(round(imc, 1)))