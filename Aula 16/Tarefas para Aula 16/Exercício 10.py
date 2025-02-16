vetor = []
subVetor = []

n = int(input("Informe valor de n: "))

for i in range(n):
    idade = int(input("Insira a idade: "))
    altura = float(input("Insira a altura: "))
    subVetor = [idade,altura]
    vetor.append(subVetor)

for i in vetor:
    i = i.reverse()

print(vetor)