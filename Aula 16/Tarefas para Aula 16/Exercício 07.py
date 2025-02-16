vetor = []
n = int(input("Informe valor de n: "))

for i in range(n):
    nota = float(input("Insira uma nota: "))
    vetor.append(nota)

print(sum(vetor) / float(len(vetor)))