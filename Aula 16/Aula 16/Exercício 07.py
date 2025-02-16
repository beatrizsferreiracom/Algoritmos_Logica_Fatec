#7) Criar um programa que leia um número N do usuário.
#Declare um vetor de tamanho N de caracteres.
#Utilize um FOR SEM UTILIZAR append para ler N nomes do usuário.
#Peça para o usuário informar uma letra L
#Utilize outro for para contar quantos nomes começam com a letra L que o usuário informou.

quantidade = int(input("Informe a quantidade de nomes: "))

vetor = [0] * quantidade
contador = 0

for i in range(quantidade):
    nome = str(input(f"Digite o {i+1}º nome: "))
    vetor[i] = nome

inicial = input('Informe a inicial: ')

for i in vetor:
    if i.startswith(inicial):
        contador += 1

print(contador, 'começam com a letra', inicial)