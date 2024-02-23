#1) Print: Olá mundo!

print ("Olá mundo!")

#2) Seu nome

nome = input("Digite seu nome: ")

print ("Olá " + nome + "! Seja bem-vindo(a)!")

#3)Mensagem multilinha

print ("Espero aprender em python:")
print ("- Como escrever scripts eficientes.")
print ("- Análise de dados.")
print ("- Desenvolvimento web.")

#4) Cocatenação de Strings

parte1= "Python é"
parte2 = "incrível!"

print (parte1 + " " + parte2)

#5) Citação Famosa

print ("Albert Einstein uma vez disse: A imaginação é mais importante que o conhecimento.")

#6) Operações matemáticas simples

print ("Soma:", 5 + 3)
print ("Subtração:", 10 - 2)
print ("Multiplicação:", 4 * 2)
print ("Divisão:", 16 / 2)

#7) Listando Informações

print ("Nome: Beatriz Ferreira")
print ("Idade: 18")
print ("Cidade natal: Chapada do Norte")
print ("Linguagem favorita: Python")

#8) Formatação com .format()

nome = "Beatriz"
idade = 18

print ("Meu nome é {} e tenho {} anos." .format(nome, idade))

#9) F-Strings

nome = "Beatriz"
idade = 18

print (f"Meu nome é {nome} e tenho {idade} anos.")

#10) Tabela de multiplicação

for i in range(1, 6):
    for j in range (1, 6):
        print(f"{i} x {j} = {i*j} ")

    print ("---")