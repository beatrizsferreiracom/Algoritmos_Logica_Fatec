#3) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-aexpressa apenas em dias.

print('Exemplo de preenchimento: 18 anos, 3 meses e 4 dias')
print('                                     ')

anos = int(input('Insira os anos: '))
meses = int(input('Insira os meses: '))
dias = int(input('Insira os dias: '))

total = (anos * 365) + (meses * 30) + dias

print('Você viveu um total de', total, 'dias.')