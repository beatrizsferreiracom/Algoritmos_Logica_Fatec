#7) Crie um algoritmo leia um número do usuário e exiba a tabuada do número.

numero = int(input('Digite o número: '))

for i in range(1, 11):
    print(numero, "x" , i , "=", numero * i)