#4) Experimente o programa a seguir e explique como ele funciona:

senha = input("Digite uma senha: ")

while senha != "1234":
    print("Senha incorreta!")
    senha = input("Digite a senha: novamente ")

print("Senha correta! Acesso permitido.")

#O código solicita que o usuário digite uma senha. Enquanto ela for diferente de "1234" é definida como incorreta
#O laço é repetido até a senha "1234" ser digitada, e definida como correta.