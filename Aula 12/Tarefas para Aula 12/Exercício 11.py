#11) Reescreva o 9 para mostrar o maior e o menor.


numero = int(input("Digite um número: "))
menor = numero
maior = 0

for i in range(9):
    numero = int(input("Digite um número: "))
    if numero < menor:
        menor = numero
    else:
        maior = numero

print(menor, 'é o menor número e', maior, 'é o maior número.')