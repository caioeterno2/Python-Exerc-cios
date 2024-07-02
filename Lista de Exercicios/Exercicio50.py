'''
Algoritmo que mostre quantos valores estão entre 10 e 20
'''
print(' =========================')
print(' | VALORES ENTRE 10 E 20 |')
print(' =========================')

entre = 0
not_entre = 0

for cont in range(1,11):
    val = int(input(f' Informe o {cont}* valor: '))
    if (val >= 10) and (val <= 20):
        entre = entre + 1 
    else:
        not_entre = not_entre + 1
    print(' --------')

print(f' Dos valores digitados "{entre:.0f}" estão entre 10 e 20 e "{not_entre:.0f}" não estão.')
print(' =========================')