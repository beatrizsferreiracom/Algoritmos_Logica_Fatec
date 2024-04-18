#9) Leia tempo e idade:

idade = int(input('Digite a idade: '))
tempo = int(input('Digite os anos de contribuição: '))

if idade > 65 or tempo > 35:
    aposentadoria = "100%"
else:
    aposentadoria = "75%"

print('A aposentadoria será de ' + aposentadoria)