#11) Escreva um programa que leia o preço original de um produto e a porcentagem 
#de desconto do usuário, e calcule o preço final após aplicar o desconto

precoP = float(input("Digite o preço padrão do produto: R$"))
desconto = float(input("Digite a porcentagem de desconto (ex: 10 para 10%): "))

valorDesconto = precoP * (desconto / 100)
precoF = precoP - valorDesconto

print("O preço final do produto com", desconto, "% de desconto é: R$", round(precoF, 2))