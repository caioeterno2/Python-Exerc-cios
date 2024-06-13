'''

'''
print(' ====================')
print(' | SOMA DOS VALORES |')
print(' ====================')

print(' Digite 3 valores diferentes: ')
print(' -------')

val1 = int(input(' 1* '))
val2 = int(input(' 2* '))
val3 = int(input(' 3* '))
print(' --------------------')

if val1 < val2 and val1 < val3:
    soma = val2 + val3
elif val2 < val1 and val2 < val3:
    soma = val1 + val3
elif val3 < val1 and val3 < val2:
    soma = val1 + val2

print(' A soma entre os dois maiores valores é {}'.format(soma))
print(' ====================')