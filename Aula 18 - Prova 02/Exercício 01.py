#1) Inverter um vetor sem utilizar funções prontas Python
#Escreva um programa que leia um vetor de tamanho N (informado pelo usuário) e imprima o vetor invertido.
#Por exemplo, se o vetor original for [1, 2, 3, 4, 5], o programa deve imprimir [5, 4, 3, 2, 1].

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho

for i in range(tamanho):
    valor = float(input(f"Digite o {i+1}º valor: "))
    vetor[tamanho - 1 - i] = valor

print("Vetor invertido:", vetor)
