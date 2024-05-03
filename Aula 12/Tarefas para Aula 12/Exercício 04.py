#4) Escreva um algoritmo que leia 10 números do usuário e calcule a soma desses números.

soma = 0
for i in range(10): 
    numero = int(input('Digite um número: '))
    soma += numero

print('A soma dos números é:', soma)