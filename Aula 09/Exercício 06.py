#6) Leia um número de 0 a 9 e o mostre por extenso.

numero = int(input("Digite um número de 0 a 9: "))

if numero == 0:
    print("Zero")
elif numero == 1:
    print("Um")
elif numero == 2:
    print("Dois")
elif numero == 3:
    print("Três")
elif numero == 4:
    print("Quatro")
elif numero == 5:
    print("Cinco")
elif numero == 6:
    print("Seis")
elif numero == 7:
    print("Sete")
elif numero == 8:
    print("Oito")
elif numero == 9:
    print("Nove")
else:
    print('Valor inválido!')