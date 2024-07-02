'''
Algoritmo que mostra o total de valores negativos
'''
print(' ==================')
print(' | VALOR NEGATIVO |')
print(' ==================')

neg = 0

for cont in range(1,11):
    val = int(input(f' Informe o {cont}* valor: '))
    if val < 0:
        neg = neg + 1 
    print(' -----')

print(f' O total de valores negativos é {neg:.0f}')
print(' ==================')
