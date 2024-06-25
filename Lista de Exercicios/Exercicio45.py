'''
Algoritmo que mostra os valores inteiros entre 1 e algum outro valor
'''
print(' ====================')
print(' | VALORES INTEIROS |')
print(' ====================')

val = int(input(' Informe um número: '))
print(' ---------')
print(' Valores inteiros entre 1 e {}.'.format(val))

for cont in range(1,val + 1):
    print('',cont)

print('=====================')
    