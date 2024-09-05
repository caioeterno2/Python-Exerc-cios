'''
 Leia 3 números escreva o maior deles e some com o 2° maior. - Ex. N° 28, 29 e 30
'''

print(' ========================')
print(' | MAIOR - SOMA - ORDEM |')
print(' ========================')

print(' Digite 3 valores diferentes: ')
print(' = = = = = = = =')

val_1 = int(input(' 1* valor: '))
print(' - - - - -')
val_2 = int(input(' 2* valor: '))
print(' - - - - -')
val_3 = int(input(' 3* valor: '))
print(' = = = = = = = =')

if val_1 > val_2 and val_1 > val_3:
    maior = val_1
    if val_2 > val_3:
        maior_2 = val_2
    else:
        maior_2 = val_3
elif val_2 > val_1 and val_2 > val_3:
    maior = val_2
    if val_1 > val_3:
        maior_2 = val_1
    else:
        maior_2 = val_3
elif val_3 > val_1 and val_3 > val_2:
    maior = val_3
    if val_1 > val_2:
        maior_2 = val_1
    else:
        maior_2 = val_2

soma = maior + maior_2

if val_1 < val_2 and val_1 < val_3:
    menor = val_1
    if val_2 < val_3:
        meio = val_2
        maior = val_3
    else:
        meio = val_3
        maior = val_2
elif val_2 < val_1 and val_2 < val_3:
    menor = val_2 
    if val_1 < val_3:
        meio = val_1
        maior = val_3
    else:
        meio = val_3
        maior = val_1
elif val_3 < val_1 and val_3 < val_2:
    menor = val_3
    if val_1 < val_2:
        meio = val_1
        maior = val_2
    else:
        meio = val_2
        maior = val_1
        
print(f' Maior valor: {maior}')
print(' - - - - -')
print(f' Soma - {maior} + {maior_2} = {soma}')
print(' - - - - -')
print(f' A ordem dos números é: {menor:.0f}.. {meio:.0f}.. {maior:.0f}..')
print(' ========================')
