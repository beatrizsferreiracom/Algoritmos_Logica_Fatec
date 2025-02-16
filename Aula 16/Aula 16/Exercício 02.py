#2) Crie um programa que leia N do usuário. Utilize um FOR para ler N nomes SEM utilizar o comando append
#Faça outro FOR para mostrar os nomes e as respectivas posições se a posição for ÍMPAR por exemplo:

quantidade = int(input("Informe a quantidade de nomes: "))

vetor = [0] * quantidade

for i in range(quantidade):
    nome = str(input(f"Digite o {i+1}º nome: "))
    vetor[i] = nome

for i in range(len(vetor)):
    if i % 2 != 0:
        print(f'Posição {i}. Nome: {vetor[i]}')