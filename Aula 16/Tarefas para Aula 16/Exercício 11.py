vetor = []
n = int(input("Informe valor de n: "))

for i in range(n):
    v = int(input("Informe um valor: "))
    vetor.append(v**2)

print(sum(vetor))