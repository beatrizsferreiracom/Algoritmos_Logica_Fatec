#15) Escreva um programa que leia o valor principal, a taxa de juros e o período de
#tempo (em anos) do usuário, e calcule o valor dos juros simples e o valor final a ser pago

valorP = float(input("Digite o valor principal: "))
taxaJ = float(input("Digite a taxa de juros anual (ex: 5 para 5%): "))
periodoA = int(input("Digite o período, em anos: "))

jurosS = valorP * (taxaJ / 100) * periodoA
valorF = valorP + jurosS

print("O valor dos juros simples é de:", round(jurosS, 2))
print("O valor final a ser pago é de: R$", round(valorF, 2))