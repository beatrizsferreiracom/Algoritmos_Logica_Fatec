#Extra 1) Faça um programa que calcule a atração gravitacional de 2 objetos usando a massa e a distância.

# F = G * M * m / d²

#F: força gravitacional
#G: constante de gravitação universal
#M e m: massas dos corpos
#d: distância entre os centros de gravidade dos corpos


G = 6.67430e-11  # m^3 kg^-1 s^-2

massa1 = float(input("Digite a massa do primeiro objeto (em kg): "))
massa2 = float(input("Digite a massa do segundo objeto (em kg): "))
distancia = float(input("Digite a distância entre os objetos (em metros): "))

forca = G * massa1 * massa2 / distancia**2

print('A força de atração gravitacional entre os objetos é de ', forca, 'N')