vetor = []
par = []
impar = []
n = int(input("Informe valor de n: "))

for i in range(n):
    v = int(input("Informe um valor: "))
    vetor.append(v)

for v in vetor:
    if v % 2 != 0:
        impar.append(v)

for v in vetor:
    if v % 2 == 0:
        par.append(v)

print(f"Valores pares: {par}")
print(f"Valores ímpares: {impar}")