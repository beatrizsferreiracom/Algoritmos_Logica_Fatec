#It is a good practice to import libraries at beginning of the code.
import math

#1) Crie um programa que leia x1 e x2 e veja a inclinação:

x1 = float(input('Digite o primeiro número: '))
x2 = float(input('Digite o segundo número: '))

alfa = x1**2 + x2**2

if alfa > 1.0:
    print('Inclinação positiva.')
else:
    print('Inclinação negativa.')
print('=====================================')
print('                                     ')


#2) Leia do usuário: Nota da prova, nota do trabalho e nota do seminário.

prova = float(input('Digite a nota da prova: '))
trabalho = float(input('Digite a nota do trabalho: '))
seminario = float(input('Digite a nota do seminário: '))

media = (prova * 0.4) + (trabalho * 0.3) + (seminario * 0.3)

if media >= 7.0:
    print('A média final foi de ', media, ' pontos e o aluno está aprovado.')
else:
    print('A média final foi de ', media, ' pontos e o aluno está reprovado.')
print('=====================================')
print('                                     ')


#3) Leia o preço do produto e mostre o valor do desconto.

preco = float(input('Digite o preço do produto: '))

if preco < 50.00:
    print('Seu desconto foi de 10% e o valor total é de R$' + str(preco * 0.9))
else:
    print('Seu desconto foi de 20% e o valor total é de R$' + str(preco * 0.8))
print('=====================================')
print('                                     ')


#4) Leia o salário do funcionário e calcule:

salario = float(input('Digite seu salário: R$'))

beneficio = salario * 0.1
desconto = salario * 0.06
total = salario + beneficio - desconto

if total < 1500:
    print('O imposto é de 0% e o salário é de R$' + str(round(total)))
else:
    print('O imposto é de 10% e o salário é de R$' + str(round(total * 1.1)))
print('=====================================')
print('                                     ')


#5) Leia do usuário sua idade, leia do valor do plano de saúde.

idade = int(input("Digite sua idade: "))
plano = float(input('Digite o valor do plano de saúde: R$'))

if idade >= 60:
    print('O novo valor do plano é: R$' + str(round(plano*1.22)))
else:
    print('O novo valor do plano é: R$' + str(round(plano*1.06)))
print('=====================================')
print('                                     ')


#3) Crie um programa que leia a senha do usuário.

senha = input('Digite a senha: ')

if senha == 'Aluno123':
    print('Senha correta.')
else:
    print('Senha incorreta.')
print('=====================================')
print('                                     ')


#7) Leia do usuário o valor da compra e o estado.

compra = float(input('Digite o valor da compra: R$'))
estado = input('Digite o estado para entrega: ')

if compra > 1500:
    if estado == 'SP' or "São Paulo":
        print('O imposto é de 12% e o valor final da compra é de R$' + str(round(compra * 1.12)))
    else:
        print('O imposto é de 8% e o valor final da compra é de R$' + str(round(compra * 1.08)))
else:
    print('O imposto é de 16% e o valor final da compra é de R$' + str(round(compra * 1.16)))


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
print('=====================================')
print('                                     ')


#Extra 2) Leia os valores e calcule o Δ = b² - 4ac

#Veja se existe solução R 
#Se Δ > 0 - calcule x1 e x2. Senão print(não existe solução no R)

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b**2) - (4 * a * c)

if delta > 0:
    x1 = ((-b) + math.sqrt(delta)) / 2 * a
    print('O valor de x1 é', round(x1, 2))
    x2 = ((-b) - math.sqrt(delta)) / 2 * a
    print('O valor de x2 é', round(x2, 2))
else:
    print('Não existe solução no R')

