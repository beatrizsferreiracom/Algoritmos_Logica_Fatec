#2) Crie um programa que calcule o volume de uma esfera, dado seu raio. 
#O programa deve pedir ao usuário o valor do raio (r) e, em seguida, calcular o volume usando a fórmula:

raio = float(input("Digite o raio da esfera, em cm: ")) 
volume = (4/3) * 3.1415 * raio**3 

print("O volume da esfera é de", round(volume, 2), "cm³")