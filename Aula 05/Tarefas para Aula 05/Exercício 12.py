#12) Escreva um programa que leia o valor total da conta de um restaurante e a porcentagem 
#de gorjeta desejada pelo usuário, e calcule o valor total a ser pago (conta + gorjeta)

conta = float(input("Digite o valor total da conta: "))
gorjetaP = float(input("Digite a porcentagem de gorjeta desejada (ex: 15 para 15%): "))
gorjetaV = conta * (gorjetaP/ 100)
total = conta + gorjetaV
print("O total a ser pago, incluindo a gorjeta de", gorjetaP, "%, é: R$", total)