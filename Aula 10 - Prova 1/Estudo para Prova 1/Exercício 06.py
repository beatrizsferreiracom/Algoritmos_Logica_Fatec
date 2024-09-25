#6) Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa 
#em segundos e mostre-o expresso em horas, minutos e segundos.

segundos = int(input('Insira o tempo em segundos: '))

horas = segundos / 3600
minutos = segundos / 60

print('A o tempo é de', round(horas), 'horas,', round(minutos), 'minutos e', segundos, 'segundos.')