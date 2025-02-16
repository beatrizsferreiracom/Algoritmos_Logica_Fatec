#1) Crie um vetor com as notas de um aluno em 5 disciplinas: [7.5, 6.8, 5.9, 8.3, 7.2]. 
#Depois, permita que o professor atualize a nota da terceira disciplina para 7.1
#(lembre-se, o índice começa em 0).


vetor = [7.5, 6.8, 5.9, 8.3, 7.2]
print(vetor)

posicao = int(input("Informe a posição da nota você deseja alterar: "))
nota = float(input("Informe a nova nota: "))

vetor[posicao] = nota

print(vetor)