#24) Escrever um algoritmo que lê a hora de início de um jogo e a hora do final do jogo (considerando apenas horas inteiras) 
#e calcula a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode 
#iniciar em um dia e terminar no dia seguinte.

horaI = int(input('Digite a hora inicial do jogo: '))
horaF = int(input('Digite a hora final do jogo: '))

duracao = (24 - horaI) + horaF

if horaI == horaF:
    print('A duração do jogo foi de 24 horas.')
elif horaI < horaF:
    print('A duração do jogo foi de', horaF - horaI, 'horas.')
else:
    print('A duração do jogo foi de', duracao, 'horas.')
