#4) Criar um programa que leia o valor de N do usuário
#Declare um vetor de tamanho N de números decimais (float)
#Utilize um FOR SEM UTILIZAR append para ler N números do usuário
#Utilize outro for para calcular a somatória dos número que estão em posições PARES

quantidade = int(input("Informe a quantidade de números: "))

vetor = [0] * quantidade
soma = 0

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    vetor[i] = num

for i in range(len(vetor)):
    if i % 2 == 0:
        soma += vetor[i]

print('O valor da soma é:', soma)