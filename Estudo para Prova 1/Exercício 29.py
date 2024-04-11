#29) Escrever um algoritmo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios 
#que fazem parte da avaliação. Calcular a média de aproveitamento, usando a fórmula:

#MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME)/7

#A atribuição de conceitos obedece a tabela abaixo:

#Média de Aproveitamento       Conceito
#9,0                              A
#7,5 e < 9,0                      B
#6,0 e < 7,5                      C
#4,0 e < 6,0                      D
#< 4,0                            E

#O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito 
#correspondente e a mensagem: APROVADO se o conceito for A,B ou C eREPROVADO se o conceito for D ou E.

numero = int(input('Digite o número de identificação do aluno: '))
nota1 = float(input('Digite a primeira nota: ')) 
nota2 = float(input('Digite a segunda nota: ')) 
nota3 = float(input('Digite a terceira nota: ')) 

ME = (nota1 + nota2 + nota3) / 3
MA = (nota1 + nota2 * 2 + nota3 * 3 + ME) / 7

if MA >= 9:
    conceito = 'A'
    mensagem = 'aprovado.'
elif MA >= 7.5 and MA < 9:
    conceito = 'B'
    mensagem = 'aprovado.'
elif MA >= 6 and MA < 7.5:
    conceito = 'C'
    mensagem = 'aprovado.'
elif MA >= 4 and MA < 6:
    conceito = 'D'
    mensagem = 'reprovado.'
elif MA < 4:
    conceito = 'E'
    mensagem = 'reprovado.'

print('O número de identificação do aluno é:', numero)
print('A média dos exercícios é de', round(ME,2), 'pontos.')
print('A média de aproveitamento é de', round(MA,2), 'pontos.')
print('O conceito do aluno é', conceito, 'e o aluno foi', mensagem)
