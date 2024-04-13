#Extra 1) Crie um programa que calcule o IMC do usuário e mostre o cálcule e se ela está acima do peso.

peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em m: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <=24.9:
    print('Você está no peso normal!')
elif imc > 24.9:
    print('Você está com sobrepeso!')