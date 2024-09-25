#10) Elaborar um algoritmo que lê 3 valores a,b,c e os escreve. A seguir, encontre o maior 
#dos 3 valores e o escreva com a mensagem : "É o maior ".

a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))
c = float(input('Insira o valor de C: '))

if a > b and a > c:
    print('O valor de A,', a, ', é o maior.')
elif b > a and b > c:
    print('O valor de B,', b, ', é o maior.')
elif c > a and c > b:
    print('O valor de C,', c, ', é o maior.')
else:
    print('Os valores de A, B e C são iguais:', a)
print('=====================================')
print('                                     ')