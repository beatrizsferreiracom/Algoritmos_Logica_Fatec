#23) Elaborar um algoritmo que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo. Supôr que os valores lidos 
#são inteiros e positivos. Caso os valores formem um triângulo, calcular e escrever a área deste triângulo. 
#Se não formam triângulo escrever os valores lidos. ( se a > b + c não formam triângulo algum, se a é o maior).

a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))

if a > b + c or b > a + c or c > a + b:
    print('Os valores não formam um triângulo.')
    print('Os valores inseridos são: a =', a, '; b =', b, '; c =', c)
else:
    s = (a + b + c) / 2  # semi-perímetro
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 #multiplicar por 0.5 é o mesmo que raiz quadrada
    print('A área do triângulo é: ' + str(round(area,2)) + '²')