#2) Explique o programa a seguir, em especial as funções startwith e lower.
#Depois, pesquise o endswith e adicione um novo FOR para mostrar as letras que terminam com A


# Criar um vetor para armazenar as strings
strings = []

# Ler as strings do usuário
for i in range(6):
    string = input(f"Digite a string {i+1}: ")
    strings.append(string)

# Imprimir as strings que começam com 'A'
print("Strings que começam com 'A':")
for string in strings:
    if string.lower().startswith('a'):
        print(string)

# Imprimir as strings que terminam com 'A'
print("Strings que terminam com 'A':")
for string in strings:
    if string.lower().endswith('a'):
        print(string)



