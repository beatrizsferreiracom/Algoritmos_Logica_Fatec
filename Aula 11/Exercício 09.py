#Conceito de SOMATÓRIA
#9) Escreva um algoritmo que calcule a soma dos números de 1 a 15.
#EXECUTE E EXPLIQUE PORQUE A VARIÁVEL SOMA É INICIALIZADA COM ZERO?

soma = 0
for num in range(1, 16): 
     soma += num 

print("A somatória de 1 a 15 é:", soma)


#EXPLICAÇÃO
#A cada repetição, é realizada a soma do número com o resultado anterior.
#A soma se inicia com 0, pois valores serão adicionados quando o programa ler os números contidos na range.
