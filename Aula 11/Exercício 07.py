#7) Altere o programa a seguir para mostrar os número ÍMPARES entre 1 e 20. Explique a alteração feita.

for num in range(1, 21): 
     if num % 2 != 0: 
           print (num)


#EXPLICAÇÃO
#Substituí o operador "==" (equivalente) por "!=" (diferente), indicando que:
#Se o número dividido por 2 gerar resto diferente de 0, ele é ímpar.