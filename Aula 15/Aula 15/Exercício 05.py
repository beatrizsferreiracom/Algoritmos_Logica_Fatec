#5) Faça um Programa que leia um vetor de 10 caracteres (letras)
#Faça um FOR que verifique quantas vogais estão no vetor. Imprima essas vogais presentes no vetor.

contador = 0
vetor = []

letras = []
vogais = []

for i in range(10):
    letra = input(f"Insira a {i+1}º letra: ")
    letras.append(letra)

for i in letras:
    if i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u":
        contador += 1
        vogais.append(i)

print('Há', contador, 'vogais')
print(vogais)