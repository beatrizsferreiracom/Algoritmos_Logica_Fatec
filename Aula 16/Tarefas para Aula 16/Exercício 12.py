vetorA = []
vetorB = []
vetorC = []
n = int(input("Informe valor de n: "))

for i in range(n):
    v = int(input("Informe um valor: "))
    vetorA.append(v)

for i in range(n):
    v = int(input("Informe um valor: "))
    vetorB.append(v)

for i in range(n):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])

print(vetorC)