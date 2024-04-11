#28) Escrever um algoritmo que lê a hora de início e hora de término de um jogo, ambas subdivididas em dois 
#valores distintos: horas e minutos. Calcular e escrever a duração do jogo, também em horas e minutos, 
#considerando que o tempo máximo de duração de um jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

print('Exemplo de preenchimento:')
print('O jogo começou às 18:15hr')
print('Hora inicial: 18')
print('Minutos iniciais: 15')
print('                                     ')

horaI = int(input('Digite a hora inicial: '))
minutoI = int(input('Digite os minutos iniciais: '))

horaF = int(input('Digite a hora final: '))
minutoF = int(input('Digite os minutos finais: '))

tempoI = (horaI * 60) + minutoI
tempoF = (horaF * 60) + minutoF

if horaI == horaF and minutoI == minutoF:
    print('A duração do jogo foi de 24 horas.')
elif tempoI < tempoF:
    duracao = tempoF - tempoI
    hora = duracao/60
    minuto = duracao%60
    print('A duração do jogo foi de', round(hora), 'horas e', minuto, 'minutos.')
else:
    duracao = (24 * 60 - tempoI) + tempoF
    hora = duracao/60
    minuto = duracao%60
    print('A duração do jogo foi de', round(hora), 'horas e', minuto, 'minutos.')
