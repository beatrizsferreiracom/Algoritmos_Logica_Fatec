#7) Leia do usuário o valor da compra e o estado.

compra = float(input('Digite o valor da compra: R$'))
estado = input('Digite o estado para entrega: ')

if compra > 1500:
    if estado == 'SP' or "São Paulo":
        print('O imposto é de 12% e o valor final da compra é de R$' + str(round(compra * 1.12)))
    else:
        print('O imposto é de 8% e o valor final da compra é de R$' + str(round(compra * 1.08)))
else:
    print('O imposto é de 16% e o valor final da compra é de R$' + str(round(compra * 1.16)))