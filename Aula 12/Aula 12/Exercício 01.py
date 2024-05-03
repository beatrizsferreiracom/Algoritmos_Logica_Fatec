#1) Criar um programa que leia um valor N do usuário e crie um FOR que mostre os números de N até 1.
#Dica: range(N,0,-1)

valor = int(input('Digite o valor: '))

for i in range(valor, 0, -1):
    print(i)