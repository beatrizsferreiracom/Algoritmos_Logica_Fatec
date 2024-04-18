#4) Leia um ano e mostre se é bissexto ou não.

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")