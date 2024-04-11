#14) Escreva um algoritmo que leia o código de um aluno e suas três notas. Calcule a média ponderada do aluno, considerando 
#que o peso para a maior nota seja 4 e para as duas restantes, 3. Mostre o código do aluno, suas três notas, a média calculada 
#e uma mensagem "APROVADO" se a média for maior ou igual a 5 e "REPROVADO" se a média for menor que 5.

codigo = int(input('Digite o código do aluno: '))
nota1 = float(input('Digite a primeira e a maior nota: ')) 
nota2 = float(input('Digite a segunda nota: ')) 
nota3 = float(input('Digite a terceira nota: ')) 

media = (nota1 * 0.4 + nota2 * 0.3 + nota3 * 0.3)

if media >= 5:
    print('A média é de', round(media,2), 'pontos e o aluno foi aprovado!')
else:
    print('A média é de', round(media,2), 'pontos e o aluno foi reprovado!')