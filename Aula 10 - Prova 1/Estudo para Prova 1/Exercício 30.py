#30) O departamento que controla o índice de poluição do meio ambiente mantém 3 grupos de indústrias que são altamente poluentes do 
#meio ambiente. O índice de poluição aceitável varia de 0,05 até 0,25. Se o índice sobe para 0,3 as indústrias do 1º grupo são intimadas 
#a suspenderem suas atividades, se o índice cresce para 0,4 as do 1º e 2º grupo são intimadas a suspenderem suas atividades e se o índice 
#atingir 0,5 todos os 3 grupos devem ser notificados a paralisarem suas atividades. Escrever um algoritmo que lê o índice de poluição medido
#e emite a notificação adequados diferentes grupos de empresas.

indice = float(input('Digite o valor do índice de poluição (Ex: 0.10 para 10%): '))

if indice >= 0.3 and indice < 0.4:
    print('Suspender atividades do grupo 1.')
elif indice >= 0.4 and indice < 0.5:
    print('Suspender ativides dos grupos 1 e 2.')
elif indice >= 0.5:
    print('Suspender atividades dos grupos 1, 2 e 3.')
else:
    print('O indíce está no nível aceitável.')