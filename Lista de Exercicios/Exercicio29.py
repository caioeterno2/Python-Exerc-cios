'''
Escreva um algoritmo que leia 2 times seus gols e escreva o vencedor.
'''
print(' ==================')
print(' | PLACAR DO JOGO |')
print(' ==================')

print(' Informe os times que jogaram hoje e os gols marcados:')
print(' ------------')

tim1 = str(input(' TIME: '))
gol1 = int(input(' GOLS: '))
print(' -----')

tim2 = str(input(' TIME: '))
gol2 = int(input(' GOLS: '))
print(' ------------------')

if gol1 > gol2:
    print(' O vencedor da partida de hoje foi o {} com {} gols!'.format(tim1,gol1))
elif gol2 > gol1:
    print(' O vencedor da partida de hoje foi o {} com {} gols!'.format(tim2,gol2))
else:
    print(' O resultado foi {} a {} dando empate.'.format(gol1,gol2))

print(' ==================')