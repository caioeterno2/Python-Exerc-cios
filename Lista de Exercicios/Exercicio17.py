'''
 Leia dois valores e escreva em ordem crescente. - Ex. N° 20
'''

print(' ===================')
print(' | ORDEM CRESCENTE |')
print(' ===================')

val_1 = int(input(' 1* valor: '))
print(' - - - - -')
val_2 = int(input(' 2* valor: '))
print(' = = = = = = = = = =')

if val_1 > val_2:
    print(f' {val_2}.. {val_1}..')
else:
    print(f' {val_1}.. {val_2}..')

print(' ===================')