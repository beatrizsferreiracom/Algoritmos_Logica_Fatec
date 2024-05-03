#2) Pergunte para o usuário o valor de N. Faça o for para apenas ler N notas do usuário.

quantidade = int(input('Digite quantas notas serão lidas: '))

for i in range(quantidade):
    notas = float(input('Digite uma nota: '))