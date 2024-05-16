#8) Teste o programa a seguir e explique como ele funciona:

operacao = ""

while operacao != "sair":
    operacao = input("Digite 'soma' para somar, 'multiplicacao' para multiplicar ou 'sair' para encerrar: ").lower()

    if operacao == "soma":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"A soma de {num1} e {num2} é: {resultado}")
        print(" ")

    elif operacao == "multiplicacao":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"A multiplicação de {num1} e {num2} é: {resultado}")
        print(" ")

    elif operacao == "sair":
        print("Encerrando a calculadora...")

    else:
        print("Operação inválida. Tente novamente.")
        print(" ")



#O programa lê do usuário a operação que ele deseja fazer e executa.
#"soma" executa a soma de dois números lidos do usuário.
#"multiplicacao" executa a multiplicação de dois números lidos do usuário.
#"sair" encerra o programa.
#Outro valor inserido no começo é lido como inválido.