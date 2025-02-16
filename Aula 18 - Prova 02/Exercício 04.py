#4) Verificar sequência crescente
#Escreva um programa que leia um vetor de tamanho N (informado pelo usuário) e verifique se os elementos estão em ordem crescente.
#O programa deve imprimir "True" se os elementos estiverem em ordem crescente e "False" caso contrário.

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho

for i in range(tamanho):
    valor = float(input(f"Digite o {i+1}º valor: "))
    vetor[i] = valor

crescente = True

for i in range(tamanho - 1):
    if vetor[i] > vetor[i + 1]:  
        crescente = False
        break

if crescente:
    print("True")
else:
    print("False")
