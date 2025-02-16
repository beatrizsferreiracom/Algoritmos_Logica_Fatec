#3) Remover elementos duplicados
#Escreva um programa que leia um vetor de tamanho N (informado pelo usuário) e remova todos os elementos duplicados do vetor.
#O programa deve imprimir o vetor resultante.
#Por exemplo, se o vetor original for [1, 2, 3, 1, 4, 2, 5], o programa deve imprimir [1, 2, 3, 4, 5].

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho

for i in range(tamanho):
    valor = float(input(f"Digite o {i+1}º valor: "))
    vetor[i] = valor

duplicatas = list(set(vetor))

print("Vetor sem duplicatas:", duplicatas)





