vetor = []
consoantes = 0

for i in range(10):
    c = input("Insira um caracter: ")
    if c != "a" and c != "e" and c != "i" and c != "o" and c != "u":
        vetor.append(c)
        consoantes += 1

print(consoantes)
print(vetor)