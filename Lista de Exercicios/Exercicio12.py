'''
Escreva um algoritmo que leia e escreva se um valor é positivo ou negativo (considere 0 positivo).
'''
print(' ====================')
print(' POSITIVO OU NEGATIVO')
print(' ====================')

val = float(input(' Digite um número: '))
print(' --------------------')

if val >= 0:
    print(' O valor {:.0f} é um número POSITIVO'.format(val))
else:
    print(' O valor {:.0f} é um número NEGATIVO'.format(val))

print(' ====================')
