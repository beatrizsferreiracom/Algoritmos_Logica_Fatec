vetor = []

for i in range(4):
    n = float(input("Insira uma nota: "))
    vetor.append(n)

print(sum(vetor) / float(len(vetor)))