#8) Um sistema de equações lineares: 
#ax + by = c 
#dx + ey = f
#Escreva um algoritmo que lê os coeficientes a,b,c,d,e e f e calcula e mostra os valores de x e y.

a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))
d = int(input('Insira o valor de d: '))
e = int(input('Insira o valor de e: '))
f = int(input('Insira o valor de f: '))

x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print('O valor de x é', round(x,2), ', e de y é', round(y,2))