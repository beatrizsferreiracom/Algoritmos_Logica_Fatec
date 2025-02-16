vetor = []

n = int(input("Informe valor de n: "))

for i in range(n):
    nota = float(input("Insira uma nota: "))
    vetor.append(nota)

for i in range(len(vetor)):
    if vetor[i] < 6:
        print(f"{i} - Nota baixa")
    else:
        print(f"{i} - Nota alta")