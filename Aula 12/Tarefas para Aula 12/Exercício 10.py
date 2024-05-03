#10) Reescreva o 9 para o menor.

numero = int(input("Digite um número: "))
menor = numero

for i in range(9):
    numero = int(input("Digite um número: "))
    if numero < menor:
        menor = numero

print(menor, 'é o menor número.')