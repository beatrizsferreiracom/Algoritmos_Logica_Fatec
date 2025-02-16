#9) Criar um programa que leia um número N do usuário.
#Declare um vetor de tamanho N de números inteiros.
#Utilize um FOR SEM UTILIZAR append para ler N números do usuário.
#Utilize outro for para contar quantos números pares estão presentes em posições impares do vetor.

quantidade = int(input("Informe a quantidade de números: "))

contador = 0
vetor = [0] * quantidade

for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    vetor[i] = num

for i in range(len(vetor)):
    if i % 2 != 0:
        if vetor[i] % 2 == 0:
            contador += 1

print(contador, 'valores são pares em posições ímpares.')