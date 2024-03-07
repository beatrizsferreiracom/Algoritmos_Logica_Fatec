#EXERCÍCIOS DE 29/02/2024

#1) Input

print ('Eu sou d+!')

nome = input('Informe nome: ') + ' ' + input('Informe sobrenome: ')
print ('Seu nome, ' + nome + ', é lindo!')

#2) Input

print ('QUESTIONÁRIO')

N = input ('Informe seu nome: ')
I = input ('Informe sua idade: ')
C = input ('Informe sua cidade: ')

print ('Nome: ' + N)
print ('Idade: ' + I)
print ('Cidade ' + C)

#3) Int

I = int(input('Qual sua idade: '))
ANO = 2024 - I

print ('Ano aproximado de nascimento: ' + str(ANO))

#4) Perguntar a idade
#Calcular: dias = idade * 365
#Dar a mensagem apropriada

I = int(input("Insira sua idade: "))
dias = 365 * I

print('Você viveu aproximadamente ' + str(dias) + ' dias.')

#5) Perguntar para o usuário o total de reais
#Calcular quantos centavos são: centavos = reais * 100

reais = int(input('Insira o valor: R$'))
centavos = reais * 100

print ('O valor em centavos é de: R$' + str(centavos))

#6) Leia do usuário um valor em dólares e converta para real

dolar = float(input('Insira o valor em dólares: US$'))
real = dolar * 4.97

print ('O valor em é real é de: R$' + str(real))

#7) Leia um número inteiro do usuário na variável N1
#Leia outro número do usuário na variável N2
#Calcule a soma das 2 variáveis: soma = N1 + N2

N1 = float(input('Insira o valor 1: '))
N2 = float(input('Insira o valor 2: '))

soma = N1 + N2

print('O total da soma é: ' + str(soma))

#8) Leia do usuário o tamanho de um lado do quadrado e cácule a área

lado = float(input('Insira o tamanho do lado (em cm): '))
area = lado * 4

print ('A área do quadrado é de ' + str(area) + ' centímetros.')

#9) Leia um número float do usuário na variável Número1
#Leia outro número float do usuário variável Número2
#Calcule a multiplicação das 2 variáveis: resultado = Número1 * Número2

Número1 = float(input('Insira o valor 1: '))
Número2 = float(input('Insira o valor 2: '))
multi = Número1 * Número2

print('O total da multiplicação é: ' + str(multi))

#PB - Leia do usuário um valor em dólares e converta para real

dolar = float(input('Insira o valor em dólares: US$'))
real = dolar * 4.97

print ('O valor em é real é de: R$' + str(real))

#PC - Leia do usuário o tamanho de um lado do quadrado e cácule a área

lado = float(input('Insira o tamanho do lado (em cm): '))
area = lado * 4
print ('A área do quadrado é de ' + str(area) + ' centímetros.')

#PD - Leia do usuário a sua idade e mostre quantas horas já viveu

idade = int(input('Insira a sua idade: '))
ano = 24 * 365
horas = idade * ano

print ('Você já viveu aproximadamente ' + str(horas) + ' horas.')
