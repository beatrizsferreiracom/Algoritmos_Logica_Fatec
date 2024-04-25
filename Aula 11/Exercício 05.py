#Alterar o programa a seguir, da tabuada do 5, para uma versão geral.
#Pergunte para o usuário qual a tabuada que ele quer e utilize no lugar do 5

numero = int(input('Insira o número referente à tabuada a ser usada: '))

for i in range(1, 11): 
    resultado = numero * i 
    print(str(resultado))

