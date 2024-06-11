'''
Escreva um algoritmo que leia dois valores e escreva o maior deles
'''
print(' ===============')
print(' | VALOR MAIOR |')
print(' ===============')

val1 = float(input(' Digite um valor: '))
print(' -----')
val2 = float(input(' Digite um segundo valor: '))
print(' ---------------')

if val1 > val2:
    print(' O número {:.0f} é maior que o número {:.0f}.'.format(val1,val2))
elif val1 == val2:
    print(' Os números são iguais.')
else:
    print(' O número {:.0f} é maior que o número {:.0f}.'.format(val2,val1))

print(' ===============')