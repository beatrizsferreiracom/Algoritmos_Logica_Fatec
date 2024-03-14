#EXERCÍCIOS DO DIA 07/03/2024

#1)Faça um um programa que:
#Leia do usuário o raio do círculo
#Calcule área: area = 3,1415 * raio * raio
#Mostre a área com mensagem apropriada

raio = float(input('Digite o raio do círculo em cm: '))

area = 3.1415 * (raio * raio)

print('A área do círculo é de ' + str(area) + ' cm².')
print('=====================================')
print('                                     ')


#2) Faça um programa que:
#Leia do usuário a nota1
#Leia do usuário a nota2
#Calcule a média como: media = nota1 * 0.5 + nota2 * 0.5
#Mostre a mensagem apropriada

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 * 0.5) + (nota2 * 0.5)

print('A média final é de ' + str(media) + ' pontos.')
print('=====================================')
print('                                     ')


#3) Faça um programa que leia
#Nota do TCC, Nota da prova, Nota do trabalho
#Calcule a media: TCC * 0.3 + prova * 0.5 + trabalho * 0.2

TCC = float(input('Digite a nota do TCC: '))
prova = float(input('Digite a nota da prova: '))
trab = float(input('Digite a nota do trabalho: '))

media = (TCC * 0.3) + (prova * 0.5) + (trab * 0.2)

print('A média final foi de ' + str(media) + ' pontos.')
print('=====================================')
print('                                     ')


#4) Faça um programa que leia o total da conta do restaurante.
#Calcule a gorjeta de 10%: gorjeta = total * 10/100
#Calcule a conta com a gorjeta: conta = total + gorjeta
#Mostre o resultado

total = float(input('Insira o valor da conta: R$'))
gorjeta = total * (10/100)
conta = total + gorjeta

print('O valor a ser pago é: R$' + str(round(conta, 2)))
print('=====================================')
print('                                     ')


#5) Faça um programa que leia: peso, altura
#Calcule o IMC = peso : altura²

peso = float(input('Digite so peso em kg: '))
altura = float(input('Digite a altura em m: '))

imc = peso / (altura * altura)

print('O valor do IMC é: ' + str(round(imc, 1)))
print('=====================================')
print('                                     ')


#6) Faça um programa que leia: O total da compra, o valor do desconto, o valor dos juros
#Calcule a conta total: conta = total – desconto + juros

total = float(input('Insira o valor da compra: R$'))
desconto = float(input('Insira o valor do desconto: R$'))
juros = float(input('Insira o valor dos juros: R$'))

conta = total - desconto + juros

print('O valor total da conta é de: R$' + str(conta))
print('=====================================')
print('                                     ')


#7) Faça um programa que leia uma distância em metros e mostre: 
#Em centímetros, em milímetros

metro = float(input('Digite a distância percorrida: '))

centimetros = metro * 100
milimetros = metro * 1000

print('A distância percorrida é de ' + str(centimetros) + ' centímetros ou ' + str(milimetros) + ' milímetros.' )
print('=====================================')
print('                                     ')


#8) Faça um programa que leia: nome, nome do meio, sobrenome
#Mostre o nome completo com as palavras separadas por um espaço em branco.

nome = input('Digite o primeiro nome: ')
nomeMeio = input('Digite o nome do meio: ')
sobrenome = input('Digite o sobrenome: ')

nomeC = nome + ' ' + nomeMeio + ' ' + sobrenome

print(nomeC)
print('=====================================')
print('                                     ')


#9) Faça um programa que leia do usuário o salário.
#Calcule: imposto = salario * 0.15
#Calcule: inss = salario * 0.17
#Calcule: valor = salario – imposto – inss
#Mostrar a mensagem adequada

salario = float(input('Digite o salário: R$'))

imposto = salario * 0.15
inss = salario * 0.17
valor = salario - imposto - inss

print('O valor do salário líquido é de: R$' + str(valor))
print('=====================================')
print('                                     ')


#Extra 1: Faça um programa que leia do usuário a temperatura em Celsius e mostre em Fahrenheit.

celsius = float(input('Insira a temperatura em graus Celsius: '))

fah = (celsius * 1.8) + 32

print('A temperatura em Fahrenheit é de ' + str(fah) + '°F')
print('=====================================')
print('                                     ')


#Extra 2: Faça uma programa que calcule Δ da fórmula de Bhaskara:
#Δ = b² = 4ac

A = float(input('Insira o valor de A: '))
B = float(input('Insira o valor de B: '))
C = float(input('Insira o valor de C: '))

bhaska = (B * B) - 4 * A * C

print('O valor de Δ é: ' + str(bhaska))
print('=====================================')
print('                                     ')


#Extra 3) Faça um programa que leia um valor em reais e mostre o total em:
#Dólares, euros, pesos, ienes

real = float(input('Insira o valor: R$'))

dolar = real / 4.93
euro = real / 5.40
pesos = real / 0.0058
iene = real / 0.033

print('O valor em dólares é: US$' + str(round(dolar, 2)))
print('O valor em euros é: €' + str(round(euro, 2)))
print('O valor em pesos é: AR$' + str(round(pesos, 2)))
print('O valor em ienes é: ¥' + str(round(iene, 2)))

