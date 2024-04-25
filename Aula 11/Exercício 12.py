#12) Altere o programa anterior que realiza a soma das idade, para que ele calcule a MÉDIA das idades.

soma = 0
for i in range(1, 6): 
    idade = int(input('Digite a idade: '))
    soma += idade

media = soma / 5

print('A soma das idades é:', media)