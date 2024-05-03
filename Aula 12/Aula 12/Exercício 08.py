#8) Crie um programa que:
#Leia o valor de X
#Faça o FOR e leia X notas de provas, faça a somatória e calcule a média das provas
#Leia o valor de Y
#Faça o FOR e leia Y notas de trabalho, faça a somatória e calcule a média dos trabalhos
#Calcula e mostre a média bimestral

somaProva = 0
somaTrabalho = 0

quantidadeProva = int(input('Digite quantas notas de prova serão lidas: '))

for i in range(quantidadeProva):
    notas = float(input('Digite a nota da prova: '))
    somaProva += notas

mediaProva = somaProva/quantidadeProva

quantidadeTrabalho = int(input('Digite quantas notas de trabalho serão lidas: '))

for i in range(quantidadeTrabalho):
    notas = float(input('Digite a nota do trabalho: '))
    somaTrabalho += notas

mediaTrabalho = somaTrabalho/quantidadeTrabalho

mediaBimestre = (0.3 * mediaTrabalho) + (0.7 * mediaProva)

print('A média bimestral do aluno é de', round(mediaBimestre, 2), 'pontos.')