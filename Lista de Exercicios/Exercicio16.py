'''
 Leia dois valores e escreva o maior deles. - Ex. N° 19
'''

print(' ===============')
print(' | MAIOR VALOR |')
print(' ===============')

val_1 = int(input(' 1* valor: '))
print(' - - - - -')
val_2 = int(input(' 2* valor: '))
print(' = = = = = = = =')

if val_1 > val_2:
    print(f' Número {val_1} maior que {val_2}')
elif val_1 == val_2:
    print(' Números são iguais.')
else:
    print(f' Número {val_2} maior que {val_1}')

print(' ===============')