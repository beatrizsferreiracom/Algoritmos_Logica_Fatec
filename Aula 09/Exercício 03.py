#3) Leia 3 valores e mostre-os em ordem crescente utilizando if.

a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))

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

