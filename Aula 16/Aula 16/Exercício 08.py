#8) Criar um programa que leia um número N do usuário.
#Declare um vetor de tamanho N de números inteiros.
#Utilize um FOR SEM UTILIZAR append para ler N números do usuário.
#Utilize outro for para calcular o produtório (multiplicação) dos números presentes nas posições ímpares do vetor.
#dica: inicializar a variável produtorio=1

quantidade = int(input("Informe a quantidade de números: "))

multi = 1
vetor = [0] * quantidade

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    vetor[i] = num

for i in range(len(vetor)):
    if i % 2 != 0:
        multi *= vetor[i]

print('O valor da multiplicação é:', multi)