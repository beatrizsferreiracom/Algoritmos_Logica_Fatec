#3) Crie um programa que leia o valor de N do usuário
#Declare um vetor de N posições de Strings: vetor = [""] * N
#Faça um FOR SEM append para o usuário informar N nomes no vetor: vetor[i]=nome
#Faça outro FOR para mostrar os nomes que tem mais de 5 letras

quantidade = int(input("Informe a quantidade de nomes: "))

vetor = [0] * quantidade

for i in range(quantidade):
    nome = str(input(f"Digite o {i+1}º nome: "))
    vetor[i] = nome

for i in range(len(vetor)):
    if len(vetor[i]) > 5:
        print(f'Posição {i}, {vetor[i]}')