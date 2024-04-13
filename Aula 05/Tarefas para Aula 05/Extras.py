#Tarefa 02: Considere o programa a seguir que leia o radio de uma esfera e calcule o volume:

print('                               ')
print('VOLUME ESFERA')
raio = float(input("Digite o raio da esfera, em cm: ")) 
volume = (4/3) * 3.1415 * raio**3 

print("O volume da esfera é de", round(volume, 2), "cm³")

print('===============================')
print('                               ')


#Altere esse programa para também calcular:
#Área do cubo

print('ÁREA CUBO')
ladoQ = float(input('Digite a medida do lado, em cm: '))                                                             

areaQ = 6 * (ladoQ*ladoQ)

print('A área do cubo é de', round(areaQ, 2), "cm²")

print('===============================')
print('                               ')


#Área paralelepípedo

print('ÁREA PARALELEPÍPEDO')
comprimentoR = float(input('Digite o comprimento, em cm: '))
larguraR = float(input('Digite a largura, em cm: '))
alturaR = float(input('Digite a altura, em cm: '))

areaR = 2 * (comprimentoR * larguraR + larguraR * alturaR + alturaR * comprimentoR)

print('A área do paralelepípedo é de', round(areaR, 2), 'cm²')

print('===============================')
print('                               ')


#Área esfera

print('ÁREA ESFERA')
raioE = float(input("Digite o raio, em cm: ")) 
areaE = 4 * 3.1415 * (raio * raio) 

print("A área da esfera é de", round(areaE, 2), "cm²")

print('===============================')
print('                               ')


#Área cilindro

print('ÁREA CILINDRO')
raioC = float(input("Digite o raio, em cm: ")) 
alturaC = float(input("Digite a altura, em cm: ")) 
areaC = 2 * 3.1415  * raio * (alturaC + raio)

print("A área do cilindro é de", round(areaC, 2), "cm²")

print('===============================')
print('                               ')


#Área cone

print('ÁREA CONE')
raioCo = float(input("Digite o raio, em cm: ")) 
geratrizCo = float(input("Digite a geratriz, em cm: ")) 
areaCo = 3.1415 * raioCo * (geratrizCo + raioCo)

print("A área do cone é de", round(areaCo, 2), "cm²")

print('===============================')
print('                               ')