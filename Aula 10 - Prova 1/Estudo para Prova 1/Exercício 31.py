#31) Escrever um algoritmo que calcule os sucessivos valores de E usando a série abaixo e considerando primeiro 3 termos, 
#depois 4 termos e, por fim, 5 termos:
#E = 1 + (1 / 1!) + (1 / 2!) + (1 / 3!) + (1 / 4!) + (1 / 5!)

E1 = 1 + (1 / (1 * 1)) + (1 / (2*1)) + (1 / (3*2*1))
E2 = 1 + (1 / (1 * 1)) + (1 / (2*1)) + (1 / (3*2*1) + (1 / (4*3*2*1)))
E3 = 1 + (1 / (1 * 1)) + (1 / (2*1)) + (1 / (3*2*1) + (1 / (4*3*2*1)) + (1 / (5*4*3*2*1)))

print('Os valores de E1, E2 e E3 são, respectivamente:', round(E1,2), round(E2,2), round(E3,2))