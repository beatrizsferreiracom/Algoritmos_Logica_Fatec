#3) Altere o programa para contar também as pessoas com menos de 1,50.

alturas = []

for i in range(5):
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    alturas.append(altura)

contador_maiores = 0
contador_menores = 0
for altura in alturas:
    if altura > 1.80:
        contador_maiores += 1
    if altura < 1.50:
        contador_menores += 1

print(f"{contador_maiores} pessoas têm altura superior a 1.80 metro.")
print(f"{contador_menores} pessoas têm altura inferior a 1.50 metro.")
