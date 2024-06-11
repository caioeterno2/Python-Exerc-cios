'''
Escreva um algoritmo que leia dois valores e escreva em ordem crescente
'''
print(' ===================')
print(' | ORDEM CRESCENTE |')
print(' ===================')

val1 = int(input(' Digite um valor: '))
print(' ----')
val2 = int(input(' Digite um segundo valor: '))
print(' -------------------')

if val1 > val2:
    print(' {}..{}'.format(val2,val1))
else:
    print(' {}..{}'.format(val1,val2))

print(' ===================')