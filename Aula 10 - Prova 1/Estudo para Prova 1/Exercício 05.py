#5) Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno. 
#Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5) 

print('A média final é de ' + str(media) + ' pontos.')