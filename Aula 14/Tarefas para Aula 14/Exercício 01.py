#1) Crie um programa que leia um valor N do usuário e mostre os números de N até 1.

numero = int(input("Digite um número: "))

if numero > 0:
    while numero >= 1:
        print(numero)
        numero -= 1
else:
    print("Valor inválido inserido! Número menor ou igual a 0.")
