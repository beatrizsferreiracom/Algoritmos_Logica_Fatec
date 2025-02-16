#5) Mover zeros para o final
#Escreva um programa que leia um vetor de tamanho N (informado pelo usuário) e mova todos os elementos iguais a zero para o 
#final do vetor, preservando a ordem dos demais elementos não-zero.
#Por exemplo, se o vetor original for [0, 1, 0, 3, 12], o programa deve modificar o vetor para [1, 3, 12, 0, 0].

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho

for i in range(tamanho):
    valor = float(input(f"Digite o {i+1}º valor: "))
    vetor[i] = valor

contador = 0  

for i in range(tamanho):
    if vetor[i] != 0:
        vetor[contador] = vetor[i]
        contador += 1
        
for i in range(contador, tamanho):
    vetor[i] = 0

print(vetor)
