#18. Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio no último ano. 
#Faça um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela abaixo.
#Mostre uma mensagem informando o saldo médio e o valor do crédito. (use o comando caso-de e não faça repetições)

#Saldo médio      Percentual
#de 0 a 200       nenhum crédito
#de 201 a 400     20% do valor do saldo médio
#de 401 a 600     30% do valor do saldo médio
#acima de 601     40% do valor do saldo médio

saldo = float(input('Insira o saldo médio: R$'))

if saldo <= 200:
    credito = 0
elif saldo >= 201 and saldo <= 400:
    credito = saldo * 0.2
elif saldo >= 201 and saldo <= 600:
    credito = saldo * 0.3
elif saldo >= 601:
    credito = saldo * 0.4

total = saldo + credito

print('O valor do saldo médio é de R$' + str(round(saldo,2)) + ' com acréscimo de R$' + str(round(credito,2)) + ' de crédito.')
print('Valor total final: R$' + str(round(total, 2)))