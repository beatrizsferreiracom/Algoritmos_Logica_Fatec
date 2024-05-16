#9) Adicione no exercício anterior as operações de DIVISÃO e SUBTRAÇÃO. 
#Coloque um IF para não permitir divisão por zero

operacao = ""

while operacao != "sair":
    operacao = input("Digite 'soma' para somar, 'subtracao' para subtrair, 'multiplicacao' para multiplicar, 'divisao' para dividir ou 'sair' para encerrar: ").lower()

    if operacao == "soma":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"A soma de {num1} e {num2} é: {resultado}")
        print(" ")

    elif operacao == "subtracao":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"A subtração de {num1} e {num2} é: {resultado}")
        print(" ")

    elif operacao == "multiplicacao":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"A multiplicação de {num1} e {num2} é: {resultado}")
        print(" ")

    elif operacao == "divisao":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"divisão de {num1} e {num2} é: {resultado}")
            print(" ")
        else: 
            print('Não é possível dividir por 0.')
            print(" ")
    
    elif operacao == "sair":
        print("Encerrando a calculadora...")

    else:
        print("Operação inválida. Tente novamente.")
        print(" ")