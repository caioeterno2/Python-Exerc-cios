'''
 Leia 2 times seus gols e escreva o vencedor. - Ex. N° 32
'''

print(' ==================')
print(' | PLACAR DO JOGO |')
print(' ==================')

print(' Informe os times que jogaram e os gols marcados:')
print(' = = = = = = = = = ')

time_1 = str(input(' 1* Time: '))
gol_1 = int(input(' Gols: '))
print(' - - - -')

time_2 = str(input(' 2* Time: '))
gol_2 = int(input(' Gols: '))
print(' = = = = = = = = = ')

if gol_1 > gol_2:
    print(f' O vencedor da partida de hoje foi o {time_1} com {gol_1} gols!')
elif gol_2 > gol_1:
    print(f' O vencedor da partida de hoje foi o {time_2} com {gol_2} gols!')
else:
    print(f' O resultado foi {gol_1} a {gol_2} dando empate.')

print(' ==================')