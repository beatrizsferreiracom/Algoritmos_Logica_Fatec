#2) Leia do usuário: Nota da prova, nota do trabalho e nota do seminário.

prova = float(input('Digite a nota da prova: '))
trabalho = float(input('Digite a nota do trabalho: '))
seminario = float(input('Digite a nota do seminário: '))

media = (prova * 0.4) + (trabalho * 0.3) + (seminario * 0.3)

if media >= 7.0:
    print('A média final foi de ', media, ' pontos e o aluno está aprovado.')
else:
    print('A média final foi de ', media, ' pontos e o aluno está reprovado.')