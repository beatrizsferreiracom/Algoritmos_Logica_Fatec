import math

vetor = []
n = int(input("Informe valor de n: "))

for i in range(n):
    v = int(input("Informe um valor: "))
    vetor.append(v)

print(f"Soma: {sum(vetor)}")
print(f"Multiplicação: {math.prod(vetor)}")