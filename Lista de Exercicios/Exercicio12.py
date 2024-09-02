'''
 Leia e escreva se um valor é positivo ou negativo (considere 0 positivo). - Ex. N° 15
'''

print(' ========================')
print(' | POSITIVO OU NEGATIVO |')
print(' ========================')

val = int(input(' Digite um número (inteiro): '))
print(' - - - - - - - - - - - - ')

if val >= 0:
    print(f' O {val} é um número POSITIVO.')
else:
    print(f' O {val} é um número NEGATIVO.')

print(' ========================')
