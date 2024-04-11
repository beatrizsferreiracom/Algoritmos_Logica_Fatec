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

tempoI = horaI + minutoI
tempoF = horaF + minutoF

duracao = tempoF - tempoI

if horaI == horaF and minutoI == minutoF:
    print('A duração do jogo foi de 24 horas.')
else:
    print('A duração do jogo foi de', duracao, 'horas.')