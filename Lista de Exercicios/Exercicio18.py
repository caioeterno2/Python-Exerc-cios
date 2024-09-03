'''
 Leia as horas de início e fim de um jogo de xadrez e calcule a duração do jogo. - Ex. N° 21 
'''

print(' ==================')
print(' | JOGO DE XADREZ |')
print(' ==================')

inicio = int(input(' Início: '))
print(' - - - -')
fim = int(input(' Fim: '))
print(' = = = = = = = = = ')

if inicio > fim:
    total_h = (24 - inicio) + fim
elif inicio < fim:
    total_h = fim - inicio
elif inicio == fim:
    total_h = 24

print(f' Total de horas jogadas: {total_h} horas')
print(' ==================')