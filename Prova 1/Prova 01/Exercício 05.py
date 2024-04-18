#5) Escreva um programa que solicite ao usuário três valores representando os comprimentos dos lados de um suposto triângulo. 
#O programa deve, então, verificar se é possível formar um triângulo com esses comprimentos e, em caso afirmativo, 
#classificar o tipo de triângulo formado.

#As regras para formação de um triângulo são:
 
#- A soma dos comprimentos de quaisquer dois lados deve ser maior que o comprimento do terceiro lado.
#- Nenhum dos comprimentos pode ser negativo ou zero. 

#Se os comprimentos fornecidos atenderem a essas regras, o programa deve classificar o tipo de triângulo formado 
#com base nos seguintes critérios:

#- Triângulo Equilátero: Todos os lados têm o mesmo comprimento.
#- Triângulo Isósceles: Dois lados têm o mesmo comprimento, mas o terceiro lado tem comprimento diferente.
#- Triângulo Escaleno: Todos os lados têm comprimentos diferentes.


a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Os valores não formam um triângulo.')

elif a < b + c or b < a + c or c < a + b:
    if a == b == c:
        print('O triângulo é Equilátero.')
    elif a == b or b == c or a == c:
        print('O triângulo é Isósceles.')
    else:
        print('O triângulo é Escaleno.')
else:
    print('Os valores não formam um triângulo.')