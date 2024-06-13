'''
Escreva um algoritmo que leia 3 números e escreva o maior deles 
'''
print(' ===============')
print(' | MAIOR VALOR |')
print(' ===============')

print(' Digite 3 valores diferentes: ')
print(' --------')

val1 = int(input(' 1* '))
val2 = int(input(' 2* '))
val3 = int(input(' 3* '))
print(' ---------------')

if val1 > val2 and val1 > val3:
    maior = val1
elif val2 > val1 and val2 > val3:
    maior = val2
elif val3 > val1 and val3 > val2:
    maior = val3

print(' O maior valor é {}'.format(maior))
print(' ===============')
