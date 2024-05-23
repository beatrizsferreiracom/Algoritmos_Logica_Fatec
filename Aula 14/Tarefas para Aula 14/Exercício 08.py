#8) Crie um programa que:
#Leia o valor de X.
#Faça o laço de repetição e leia X notas de provas, faça a somatória e calcule a média das provas.
#Leia o valor de Y.
#Faça o laço de repetição e leia Y notas de trabalho, faça a somatória e calcule a média dos trabalhos.
#Calcula a média bimestral = 0.3 * MEDIATRABALHO + 0.7 * MEDIAPROVA.
#Mostre a média bimestral


contadorP = 1
contadorT = 1
somaProva = 0
somaTrabalho = 0

quantidadeProva = int(input('Digite quantas notas de prova serão lidas: '))

while(quantidadeProva >= contadorP):
    notas = float(input('Digite a nota da prova: '))
    contadorP += 1
    somaProva += notas

mediaProva = somaProva/quantidadeProva

quantidadeTrabalho = int(input('Digite quantas notas de trabalho serão lidas: '))

while(quantidadeTrabalho >= contadorT):
    notas = float(input('Digite a nota do trabalho: '))
    contadorT += 1
    somaTrabalho += notas

mediaTrabalho = somaTrabalho/quantidadeTrabalho

mediaBimestre = (0.3 * mediaTrabalho) + (0.7 * mediaProva)

print('A média bimestral do aluno é de', round(mediaBimestre, 2), 'pontos.')