#2) Pergunte para o usuário o valor de N. Faça ler N notas do usuário.

contador = 1
quantidade = int(input('Digite quantas notas serão lidas: '))

while(quantidade >= contador):
    notas = float(input('Digite uma nota: '))
    contador += 1