vetor = []
vogais = 0

for i in range(10):
    c = input("Insira um caracter: ")
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        vetor.append(c)
        vogais += 1

print(vogais)
print(vetor)