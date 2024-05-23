#8) Explique o append, o sum e o len

notas = []

for i in range(5):
    nota = float(input(f"Digite a nota da disciplina {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média aritmética das notas é: {media:.2f}")


#O vetor/lista "notas" está vazio
#A repetição do laço for acontecerá 5 vezes, como foi definido
#São pedidas 5 notas ao usuário
#"append" adiciona cada nota digitada no final da litsa, pela ordem inserida
#"sum" realiza a soma dos valores
#"len" lê quantos valores foram inseridos ao vetor