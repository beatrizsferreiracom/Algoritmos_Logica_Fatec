#26) Escrever um algoritmo que lê um valor em reais e calcula qual o menor número possível de notas de 100, 50, 10, 5 e 2
#em que o valor lido pode ser decomposto. Escrever o valor lido e a relação denotas necessárias.

valor = int(input('Insira o valor total: R$'))

cem = valor // 100
resto = valor % 100

cinquenta = resto // 50
resto %= 50

dez = resto // 10
resto %= 10

cinco = resto // 5
resto %= 5

dois = resto // 2
resto %= 2

print("Valor lido:", valor, "reais")
print("Notas necessárias:")
print("Notas de 100:", cem)
print("Notas de 50:", cinquenta)
print("Notas de 10:", dez)
print("Notas de 5:", cinco)
print("Notas de 1:", dois)

