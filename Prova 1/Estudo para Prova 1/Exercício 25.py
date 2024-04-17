#25) Escrever um algoritmo que lê um conjunto de 4 valores i, a, b, c, onde i é um valor inteiro e positivo e 
#a, b, c, são quaisquer valores reais e os escreva. A seguir:

#a) Se i=1 escrever os três valores a, b, c em ordem crescente.
#b) Se i=2 escrever os três valores a, b, c em ordem decrescente.
#c) Se i=3 escrever os três valores a, b, c de forma que o maior entre a, b, c fique dentre os dois.


i = int(input('Insira o valor de i: '))
a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))

if i == 1:
    if a <= b <= c:
        print(a, b, c)
    elif c <= a <= b:
        print(c, a, b)
    elif a <= c <= b:
        print(a, c, b)
    elif b <= a <= c:
        print(b, a, c)
    elif b <= c <= a:
        print(b, c, a)
    else:
        print(c, b, a)


elif i == 2:
    if a >= b >= c:
        print(a, b, c)
    elif c >= a >= b:
       print(c, a, b)
    elif a >= c >= b:
        print(a, c, b)
    elif b >= a >= c:
        print(b, a, c)
    elif b >= c >= a:
        print(b, c, a)
    else:
        print(c, b, a)


else:
    if a > b and a > c:
        print(b, a, c)
    elif b > c and b > a:
        print(a, b, c)
    else:
        print(a, c, b)
