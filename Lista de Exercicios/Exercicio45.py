'''
Algoritmo que mostra os valores inteiros entre 1 e algum outro valor
'''
print(' ====================')
print(' | VALORES INTEIROS |')
print(' ====================')

val = int(input(' Informe um número: '))
print(' ---------')

while val <= 0:
    val = int(input(' Informe um número maior que 0: '))
    print(' ---------')

print(' Valores inteiros entre 1 e {}.'.format(val))
print(' ---------')

for cont in range(1,val + 1):
    print('',cont)


print(' =====================')
    