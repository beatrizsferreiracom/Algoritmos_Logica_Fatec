#5) Aprimore o programa para não permitir o usuário informar um número que extrapole as dimensões do vetor.

dias = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"]
numero = int(input("Qual dia quer saber? "))

if numero > 7:
    print('Valor inválido!')
else:
    print (dias[numero - 1])