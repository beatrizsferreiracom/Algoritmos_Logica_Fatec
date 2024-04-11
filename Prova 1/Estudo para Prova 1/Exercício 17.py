#17) Tendo como dados de entrada a altura e o sexo de uma pessoa (?M? masculino e ?F? feminino),construa um algoritmo que 
#calcule seu peso ideal, utilizando as seguintes fórmulas:

#para homens: (72.7*h)-58
#para mulheres: (62.1*h)-44.7

genero = input('Insira o gênero: ')
altura = float(input('Insira a altura em metro: '))

if genero == 'Feminino' or genero == 'F':
    peso = (62.1 * altura) - 44.7
elif genero == 'Masculino' or genero == 'M':
    peso = (72.7* altura) - 58

print('O peso ideal é de', round(peso), 'kg.')