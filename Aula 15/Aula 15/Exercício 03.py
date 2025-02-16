#3) Faça um programa que pergunte o valor de N para o usuário.
#Em seguida,  leia um vetor de N números inteiros
#Depois, conte quantos números são iguais a zero, quantos números são maiores que zero e quantos números são menores que zero.

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = []
contador1 = 0
contador2 = 0
contador3 = 0

for i in range(tamanho):
    num = int(input(f"Digite o número {i+1}: "))
    vetor.append(num)

for i in vetor:
    if i == 0:
        contador1 += 1
    elif i > 0:
        contador2 += 1
    else:
        contador3 += 1

print(contador1, "números iguais a zero")
print(contador2, "números maiores que zero")
print(contador3, "números menores que zero")
