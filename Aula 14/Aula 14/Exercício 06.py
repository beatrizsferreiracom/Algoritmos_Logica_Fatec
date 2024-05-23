#6) TESTE E EXPLIQUE (para que serve)

tamanho = int(input("Digite o tamanho do vetor: "))

vetor = [0] * tamanho    #<---- o que é isso?

for i in range(tamanho):
    elemento = input(f"Digite o elemento {i+1}: ")
    vetor[i] = elemento

print("Vetor:", vetor)


#O programa pergunta ao usuário quantos elementos terá dentro do vetor.
#A operação define que 0 multiplicando a quantidade definida.
#O for soma o vetor 0 ao 1.
#Os elementos inseridos são multiplicados por 1 e adicionados ao vetor.