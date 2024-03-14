#Tarefa 01: Lista de Exercícios de Algoritmo

#1) Soma de dois números:
num1 = float(input("Digite o primeiro número: ")) 
num2 = float(input("Digite o segundo número: ")) 

soma = num1 + num2

print("O resultado da soma é", soma)


#2) Média de três notas:
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 * 0.5) + (nota2 * 0.5) + (nota3 * 0.5)

print('A média final é de ' + str(media) + ' pontos.')


#3) Converter Celsius para Fahrenheit:
celsius = float(input('Insira a temperatura em graus Celsius: '))

fah = (celsius * 1.8) + 32

print('A temperatura em Fahrenheit é de ' + str(fah) + '°F')


#4) Área de um retângulo:
largura = float(input("Digite a largura do retângulo, em cm: ")) 
altura = float(input("Digite a altura do retângulo, em cm: ")) 

area = largura * altura

print("A área do retângulo é de", round(area, 2), "cm²")


#5) Concatenar duas strings:
str1 = input('Digite a primeira string: ') 
str2 = input('Digite a segunda string: ') 

concatenada = str1 + str2

print('String concatenada:', concatenada)


#6) Contar caracteres de uma string:
string = input("Digite uma string: ")

print("A string contém", len(string), 'caracteres.')


#7) Converter metros para centímetros:
metro = float(input('Digite o valor em metros: '))

centimetro = metro * 100

print('O valor inserido é de', round(centimetro, 2), 'centímetros')
						

#8) Converter idade em anos para dias (considerando um ano com 365 dias):
anos = int(input("Insira sua idade em anos: "))
dias = 365 * anos

print('Você viveu aproximadamente', dias, 'dias.')


#9) Escreva um programa que leia o raio de um círculo do usuário e calcule sua área.
raio = float(input('Digite o raio do círculo em cm: '))

area = 3.1415 * (raio * raio)

print('A área do círculo é de ' + str(round(area, 2)) + ' cm².')


#10) Conversão de Celsius para Fahrenheit
celsius = float(input('Insira a temperatura em graus Celsius: '))

fah = (celsius * 1.8) + 32

print('A temperatura em Fahrenheit é de ' + str(fah) + '°F')


#11) Escreva um programa que leia o preço original de um produto e a porcentagem 
#de desconto do usuário, e calcule o preço final após aplicar o desconto
precoP = float(input("Digite o preço padrão do produto: R$"))
desconto = float(input("Digite a porcentagem de desconto (ex: 10 para 10%): "))

valorDesconto = precoP * (desconto / 100)
precoF = precoP - valorDesconto

print("O preço final do produto com", desconto, "% de desconto é: R$", round(precoF, 2))


#12) Escreva um programa que leia o valor total da conta de um restaurante e a porcentagem 
#de gorjeta desejada pelo usuário, e calcule o valor total a ser pago (conta + gorjeta)
conta = float(input("Digite o valor total da conta: "))
gorjetaP = float(input("Digite a porcentagem de gorjeta desejada (ex: 15 para 15%): "))
gorjetaV = conta * (gorjetaP/ 100)
total = conta + gorjetaV
print("O total a ser pago, incluindo a gorjeta de", gorjetaP, "%, é: R$", total)


#13) Escreva um programa que leia uma distância em metros do usuário 
#e a converta para centímetros, quilômetros e milímetros
metros = float(input('Digite a distância percorrida em metros: '))

centimetros = metros * 100
milimetros = metros * 1000
quilometros = metros / 1000

print('A distância percorrida em centímetros:', centimetros, 'cm')
print('A distância percorrida em milímetros:', milimetros, 'mm')
print('A distância percorrida em quilômetros:', quilometros, 'km')


#14) Cálculo de média de 3  notas
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 * 0.5) + (nota2 * 0.5) + (nota3 * 0.5)

print('A média final é de ' + str(media) + ' pontos.')


#15) Escreva um programa que leia o valor principal, a taxa de juros e o período de
#tempo (em anos) do usuário, e calcule o valor dos juros simples e o valor final a ser pago
valorP = float(input("Digite o valor principal: "))
taxaJ = float(input("Digite a taxa de juros anual (ex: 5 para 5%): "))
periodoA = int(input("Digite o período, em anos: "))

jurosS = valorP * (taxaJ / 100) * periodoA
valorF = valorP + jurosS

print("O valor dos juros simples é de:", round(jurosS, 2))
print("O valor final a ser pago é de: R$", round(valorF, 2))


#16) Escreva um programa que leia um valor em dólares (USD) do usuário e o converta 
#para euros (EUR) e reais (BRL), considerando taxas de câmbio fixas
valorD = float(input("Digite o valor em dólares (USD): "))

#Taxas de câmbio fixas
taxaE = 0.92  # 1 USD = 0.92 EURO
taxaR = 4.98  # 1 USD = 4.98 REAL

valorE = valorD * taxaE
valorR = valorD * taxaR

print('O valor em dólares, US$' + str(valorD) + ', é igual a:')
print('€' + str(round(valorE, 2)))
print('R$' + str(round(valorR, 2)))


#17) Faça um programa que leia o nome, nome do meio e sobrenome do usuário depois mostre o nome completo.
nome = input('Digite o primeiro nome: ')
nomeMeio = input('Digite o nome do meio: ')
sobrenome = input('Digite o sobrenome: ')

nomeC = nome + ' ' + nomeMeio + ' ' + sobrenome

print(nomeC)


#18) Faça um programa que leia do usuário o seu salário e calcule:
#-imposto = salario *0.15
#-inss = salario*0.17
#-valor = salario - imposto - inss
salario = float(input('Digite o salário: R$'))
imposto = salario * 0.15
inss = salario * 0.17
valor = salario - imposto - inss

print('O valor do salário líquido é de: R$' + str(valor))



#Tarefa 02: Considere o programa a seguir que leia o radio de uma esfera e calcule o volume:

print('                               ')
print('VOLUME ESFERA')
raio = float(input("Digite o raio da esfera, em cm: ")) 
volume = (4/3) * 3.1415 * raio**3 

print("O volume da esfera é de", round(volume, 2), "cm³")

print('===============================')
print('                               ')


#Altere esse programa para também calcular:
#Área do cubo

print('ÁREA CUBO')
ladoQ = float(input('Digite a medida do lado, em cm: '))                                                             

areaQ = 6 * (ladoQ*ladoQ)

print('A área do cubo é de', round(areaQ, 2), "cm²")

print('===============================')
print('                               ')


#Área paralelepípedo

print('ÁREA PARALELEPÍPEDO')
comprimentoR = float(input('Digite o comprimento, em cm: '))
larguraR = float(input('Digite a largura, em cm: '))
alturaR = float(input('Digite a altura, em cm: '))

areaR = 2 * (comprimentoR * larguraR + larguraR * alturaR + alturaR * comprimentoR)

print('A área do paralelepípedo é de', round(areaR, 2), 'cm²')

print('===============================')
print('                               ')


#Área esfera

print('ÁREA ESFERA')
raioE = float(input("Digite o raio, em cm: ")) 
areaE = 4 * 3.1415 * (raio * raio) 

print("A área da esfera é de", round(areaE, 2), "cm²")

print('===============================')
print('                               ')


#Área cilindro

print('ÁREA CILINDRO')
raioC = float(input("Digite o raio, em cm: ")) 
alturaC = float(input("Digite a altura, em cm: ")) 
areaC = 2 * 3.1415  * raio * (alturaC + raio)

print("A área do cilindro é de", round(areaC, 2), "cm²")

print('===============================')
print('                               ')


#Área cone

print('ÁREA CONE')
raioCo = float(input("Digite o raio, em cm: ")) 
geratrizCo = float(input("Digite a geratriz, em cm: ")) 
areaCo = 3.1415 * raioCo * (geratrizCo + raioCo)

print("A área do cone é de", round(areaCo, 2), "cm²")

print('===============================')
print('                               ')