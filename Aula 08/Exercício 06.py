#6) Leia a idade, renda e a experiência:

idade = int(input('Digite a idade: '))
renda = float(input('Digite a renda anual: R$'))
experiencia = int(input('Digite o nível de experiência: '))

if idade < 18:
    if experiencia < 6:
        if renda <= 1200:
            imposto = 0
        else:
            imposto = renda * 0.04
    else:
        if experiencia > 18:
            imposto = renda * 0.16
        else:
            imposto = renda * 0.14
else:
    imposto = renda * 0.22

print('O valor do imposto será de R$' + str(round(imposto, 2)))