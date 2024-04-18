#3) Leia x1, x2, y1 e y2;
#Calcular Δ1 = (x2-x1)² e Δ2 = (y2-y1)²;

x1 = float(input('Insira o valor de x1: '))
x2 = float(input('Insira o valor de x2: '))
y1 = float(input('Insira o valor de y1: '))
y2 = float(input('Insira o valor de y2: '))

delta1 = (x2 - x1)**2 
delta2 = (y2 - y1)**2

if delta1 > delta2:
    if x1 > x2:
        alfa = delta1 * (x1**2)
    else:
        alfa = delta1 * (x2**2)
else:
    alfa = (delta2 - delta1)**2

print('O valor de alfa é', round(alfa,2))