#4) Crie um programa que leia dois vetores VETA e VETB de 4 números inteiros cada.
#Depois, calcule a soma dos elementos correspondentes na mesma posição no VETC.
#Por exemplo:

#VETA= [1,4,6,4]
#VETB = [6,3,1,0]
#resultado VETC = [7, 7, 7, 4]
#dica: VETC[i] = VETA[i] + VETB[i]

vetorA = []
vetorB = []
vetorC = []

print("Valores do Vetor A")
for i in range(4):
    valor = int(input(f"Informe o valor {i+1}: "))
    vetorA.append(valor)

print("Valores do Vetor B")
for i in range(4):
    valor = int(input(f"Informe o valor {i+1}: "))
    vetorB.append(valor)

for i in range (4):
    resultado = vetorA[i] + vetorB[i]
    vetorC.append(resultado)

print(vetorC)


