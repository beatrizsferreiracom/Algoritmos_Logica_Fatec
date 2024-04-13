#6) Cácule a diagonal de um triângulo. Leia a largura e comprimento:
#diagonal= /largura² + comprimento²

import math

largura = float(input('Digite o valor da largura, em cm: '))
comprimento = float(input('Digite o valor do comprimento, em cm: '))

diagonal = math.sqrt(largura**2 + comprimento**2)

print('O valor da diagonal é de', round(diagonal,2), 'centímentros.')