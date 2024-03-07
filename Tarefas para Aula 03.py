#EXERCÍCIOS DE 01/03/2024

#1) Considere o seguinte programa que soma 2 números do tipo float. 
#Altere para que sejam lidos e somados 4 números, ao invés de somente 2 

num1 = float(input('Digite o primeiro número: ')) 
num2 = float(input('Digite o segundo número: ')) 
num3 = float(input('Digite o terceiro número: ')) 
num4 = float(input('Digite o quarto número: ')) 

soma = num1 + num2 + num3 + num4

print('A soma é ' + str(soma))

#2) Se baseie no seguinte programa que calcula a média de 3 notas. 
#Faça um programa que leia 4 médias e tire a média das 4 notas

nota1 = float(input('Digite a primeira nota: ')) 
nota2 = float(input('Digite a segunda nota: ')) 
nota3 = float(input('Digite a terceira nota: ')) 
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('A média é '+ str(media))

#3) Crie um programa que:

#1. Leia a altura do retângulo na variável altura
#2. Leia o largura do retângulo na variável largura
#3. Calcule a área do retângulo: area =  largura * altura
#4. Mostre o resultado do cálculo

altura = float(input('Insira a altura em cm: '))
largura = float(input('Insira a largura em cm: '))

area = largura * altura

print('A área do retângulo é de ' + str(area) + ' centímetros.')

#4) Considere o seguinte programa. Altere para concatenar 3 string
#Concatenar três strings:

str1 = input('Digite a primeira string: ') 
str2 = input('Digite a segunda string: ') 
str3 = input('Digite a terceira string: ')

concatenada = str1 + str2 + str3

print('String concatenada: ' + concatenada)