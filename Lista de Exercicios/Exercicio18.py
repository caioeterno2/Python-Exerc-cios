'''
Escreva um algoritmo que leia as horas de início e fim de um jogo de xadrez e calcule a duração do jogo 
'''
print(' ==================')
print(' | JOGO DE XADREZ |')
print(' ==================')

inicio = float(input(' INICIO: '))
print(' ----')
fim = float(input(' FIM: '))
print(' ------------------')


if inicio > fim:
    total = (24 - inicio) + fim
elif inicio < fim:
    total = fim - inicio
elif inicio == fim:
    total = 24

print(' O total de horas jogadas foram: H{:.0f}'.format(total))
print(' ==================')