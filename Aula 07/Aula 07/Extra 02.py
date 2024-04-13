#Extra 2) Leia os valores e calcule o Δ = b² - 4ac

#Veja se existe solução R 
#Se Δ > 0 - calcule x1 e x2. Senão print(não existe solução no R)

import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b**2) - (4 * a * c)

if delta > 0:
    x1 = ((-b) + math.sqrt(delta)) / 2 * a
    print('O valor de x1 é', round(x1, 2))
    x2 = ((-b) - math.sqrt(delta)) / 2 * a
    print('O valor de x2 é', round(x2, 2))
else:
    print('Não existe solução no R')