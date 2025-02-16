#2) Crie um vetor com os nomes de 6 contatos: ["Ana", "Bruno", "Carla", "Daniel", "Eva", "Fábio"]. 
#Peça ao usuário para substituir o quinto contato por "Elisa".
#Depois, imprima o nome do primeiro e do último contato.

vetor = ["Ana", "Bruno", "Carla", "Daniel", "Eva", "Fábio"]
print(vetor)

posicao = int(input("Informe a posição do nome você deseja alterar: "))
nome = input("Informe o novo nome: ")

vetor[posicao] = nome
print(vetor)

print(f"Primeiro contato: {vetor[0]}\nSegundo contato: {vetor[len(vetor)-1]}")