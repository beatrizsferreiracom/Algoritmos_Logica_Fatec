#6) Criar um programa que leia um número N do usuário.
#Declare um vetor de tamanho N de números inteiros.
#Utilize um FOR SEM UTILIZAR append para ler N números inteiros do usuário.
#Utilize outro for para encontrar o maior valor presente no vetor. 
#(dica: considere que o primeiro elemento do vetor, na posição 0, seja o maior e depois compare com os demais)

quantidade = int(input("Informe a quantidade de números: "))

vetor = [0] * quantidade

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    vetor[i] = num

maior = vetor [0]

for i in (vetor):
    if i > maior:
        maior = i

print(maior)