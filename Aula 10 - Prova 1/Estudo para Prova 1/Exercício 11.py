#11) Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: "São múltiplos" ou "Não são múltiplos".

a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))

if a % b == 0:
    print('Os números são múltiplos.')
else:
    print('Os números não são múltiplos.')